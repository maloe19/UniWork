import plotly.express as px
from dash import Dash, dash_table, html, dcc, Input, Output, State
import pandas as pd
import io
import base64
import dash
import datetime

app  = Dash(__name__, suppress_callback_exceptions=True) 

#htl elements
app.layout = html.Div([
    dcc.Upload(
        id='data_upload',
        children=html.Div([html.Button('Upload file')]),
        style={},
        #Uploading multiple files is allowed
        multiple=True
    ),
    html.Hr(), #a horizontal line
    html.Div(id='output'),
    html.Div(id='output_table'),
])

def parse(contents, filename, date):
    type, string_content = contents.split(',')

    decoder = base64.b64decode(string_content)
    try:
        if 'csv' in filename:
            #For uploading a CSV file
            df = pd.read_csv(io.StringIO(decoder.decode('utf-8')))
        #excel reading
        #elif 'xls' in filename:
            #df = pd.read_excel(io.BytesIO(decoder))
        #txt and tsv reading
        #elif 'txt' or 'tsv' in filename:
            #df = pd.read_csv(
                #io.StringIO(decoder.decode('utf-8')))
    except Exception as error:
        print(error)
        return html.Div(['Something went wrong'])

    return html.Div([
        html.H1(filename),
        html.H2(datetime.datetime.fromtimestamp(date)),

        html.P("Select graph"),
        dcc.RadioItems(
            id="graph_choice",
            options=[{'label': 'bar-graph', 'value': 'bar'},
                     {'label': 'heat-map', 'value': 'map'},
                     {'label': 'scatter-plot', 'value': 'scatter'}], 
                     value='bar'
        ),
        html.Hr(), 
        #drop-down with colors
        dcc.Dropdown(
            id="dropdown",
            options=['blue', 'red', 'yellow'],
            value='blue',
            style={},
        ),
        html.Hr(), 

        html.P("Pick x-axis"),
        dcc.Dropdown(id='x_axis', options=[{'label':x, 'value':x} for x in df.columns]),
        html.P("Pick y-axis"),
        dcc.Dropdown(id='y_axis', options=[{'label':x, 'value':x} for x in df.columns]),
        html.Button(id='make_graph', children="Make Graph"),
        html.Hr(),

        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'name': i, 'id': i} for i in df.columns],
            page_size=15
        ),
        dcc.Store(id='store_id', data=df.to_dict('records')),
        html.Hr(),

        #Debugging the display of the content
        html.Div('ContentRaw'),
        html.Pre(contents[0:200] + '...', style={})
    ])

#output and input
@app.callback(Output('output_table', 'children'),
                Input('data_upload', 'contents'),
                State('data_upload', 'filename'),
                State('data_upload', 'last_modified'))
def update(contentsList, filenameList, datesList):  
    if contentsList is not None:
        children = [parse(c, n, d) for c, n, d in zip(contentsList, filenameList, datesList)] 
        return children

#output and input
@app.callback(Output('output', 'children'),
            Input('make_graph', 'n_clicks'),
            State('graph_choice', 'value'),
            State('store_id', 'data'),
            State('x_axis', 'value'),
            State('y_axis', 'value')) #State("dropdown", "value"),
def graph_maker(n, chosen_graph, data , x_val, y_val): #color
    if n is None:
        return dash.no_update
    #else:
        #fig = px.bar(data, x=x_val, y=y_val)
        #return dcc.Graph(figure=fig)
    elif chosen_graph == 'bar':
        fig = px.bar(data, x=x_val, y=y_val) #, marker_color=color
        return dcc.Graph(figure=fig)
    elif chosen_graph == 'map':
        fig2 = px.density_heatmap(data, x=x_val, y=y_val) #, x_margin="histogram", y_marginal="histogram", text_auto=True
        return dcc.Graph(figure=fig2)
    elif chosen_graph == 'scatter':
        fig3 = px.scatter(data, x=x_val, y=y_val) #, marker_color=color
        return dcc.Graph(figure=fig3)

if __name__ == '__main__':
    app.run_server(debug=True) #host='0.0.0.0' og port=8000
