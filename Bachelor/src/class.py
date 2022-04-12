import plotly.express as px
from dash import Dash, dash_table, html, dcc, Input, Output, State
import pandas as pd
import io
import base64
import dash

stylesheet = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app  = Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=stylesheet) 

#htl elements
app.layout = html.Div([
    dcc.Upload(
        id='data_upload',
        children=html.Div([html.Button('Upload file'), 'or Drag and Drop']), 
        style={'textAlign': 'center'},
        #Uploading multiple files is allowed
        multiple=True
    ),
    html.Hr(), #a horizontal line
    html.Div(id='output'),
    html.Hr(),
    html.Div(id='output_table'),
])

def parse(contents, filename):
    type, string_content = contents.split(',')

    decoder = base64.b64decode(string_content)
    try:
        #For uploading a CSV file
        if 'csv' in filename:
            df = pd.read_csv(io.StringIO(decoder.decode('utf-8')))
        #excel reading
        elif 'xls' in filename:
            df = pd.read_excel(io.BytesIO(decoder))
        #txt and tsv reading
        elif 'txt' or 'tsv' in filename:
            df = pd.read_csv(io.StringIO(decoder.decode('utf-8')))
    except Exception as error:
        print(error)
        return html.Div(['Something went wrong'])

    return html.Div([
        html.H1(filename),

        html.P("Select graph"),
        dcc.RadioItems(
            id="graph_choice",
            options=[{'label': 'bar-graph', 'value': 'bar'},
                     {'label': 'heat-map', 'value': 'map'},
                     {'label': 'scatter-plot', 'value': 'scatter'}], 
                     value='bar'
        ), 

        html.P("Pick x-axis"),
        dcc.Dropdown(id='x_axis', options=[{'label':x, 'value':x} for x in df.columns]),
        html.P("Pick y-axis"),
        dcc.Dropdown(id='y_axis', options=[{'label':x, 'value':x} for x in df.columns]),
        html.Button(id='make_graph', children="Make Graph"),

        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'name': i, 'id': i} for i in df.columns],
            page_size=10
        ),
        dcc.Store(id='store_id', data=df.to_dict('records')),
    ])

#output and input
@app.callback(Output('output_table', 'children'),
                Input('data_upload', 'contents'),
                State('data_upload', 'filename'))
def update(contentsList, filenameList):  
    if contentsList is not None:
        children = [parse(c, n) for c, n in zip(contentsList, filenameList)] 
        return children

@app.callback(Output('output', 'children'),
            Input('make_graph', 'n_clicks'),
            State('graph_choice', 'value'),
            State('store_id', 'data'),
            State('x_axis', 'value'),
            State('y_axis', 'value')) 
def graph_maker(n, chosen_graph, data, x_val, y_val): 
    if n is None:
        return dash.no_update
    elif chosen_graph == 'bar':
        fig = px.bar(data, x=x_val, y=y_val) 
        return dcc.Graph(figure=fig)
    elif chosen_graph == 'map':
        fig2 = px.density_heatmap(data, x=x_val, y=y_val, marginal_x="histogram", marginal_y="histogram", text_auto=True)
        return dcc.Graph(figure=fig2)
    elif chosen_graph == 'scatter': 
        fig3 = px.scatter(data, x=x_val, y=y_val) 
        return dcc.Graph(figure=fig3)

if __name__ == '__main__':
    app.run_server(debug=True) 
