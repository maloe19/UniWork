from numpy import source
import plotly.express as px
from dash import Dash, dash_table, html, dcc, Input, Output, State
import pandas as pd
import io
import base64
import dash
#import datetime
#import plotly.graph_objects as go
#import numpy as np

#colors = px.colors.named_colorscales()
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

def parse(contents, filename): #, date
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
        #html.H2(datetime.datetime.fromtimestamp(date)),

        html.P("Select graph"),
        dcc.RadioItems(
            id="graph_choice",
            options=[{'label': 'bar-graph', 'value': 'bar'},
                     {'label': 'heat-map', 'value': 'map'},
                     {'label': 'scatter-plot', 'value': 'scatter'},
                     {'label': 'mutiple', 'value': 'analysis'}
                     ,{'label': 'destiny', 'value': 'contour'}
                     ], #,{'label': 'mapbox', 'value': 'box'}
            value='bar'
        ),
        html.Hr(), 

        #drop-down with colors                   #måske lave dropdown options som checklist ovenover!!!
        #dcc.Dropdown(
            #id="color_choice",
            #options=['blue', 'red', 'Gold'],
            #options=colors,
            #options=[{'label': 'gold', 'value': 'Gold'},
                     #{'label': 'turquoise', 'value': 'MediumTurquoise'},
                     #{'label': 'green', 'value': 'LightGreen'}], 
            #value='Gold',
            #style={},
        #),
        #html.Hr(), 

        html.P("Pick x-axis"),
        dcc.Dropdown(id='x_axis', options=[{'label':x, 'value':x} for x in df.columns]),
        html.P("Pick y-axis"),
        dcc.Dropdown(id='y_axis', options=[{'label':x, 'value':x} for x in df.columns]),
        html.Button(id='make_graph', children="Make Graph"),
        html.Hr(),
        #dcc.Dropdown(id='type', options=[{'label':x, 'value':x} for x in df.columns],className="two columns",className="row"),

        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'name': i, 'id': i} for i in df.columns],
            page_size=10
        ),
        dcc.Store(id='store_id', data=df.to_dict('records')),
        #html.Hr(),

        #Debugging the display of the content
        #html.Div('ContentRaw'),
        #html.Pre(contents[0:200] + '...', style={})
    ])

#output and input
@app.callback(Output('output_table', 'children'),
                Input('data_upload', 'contents'),
                State('data_upload', 'filename')) #State('data_upload', 'last_modified')
def update(contentsList, filenameList):#, datesList
    if contentsList is not None:
        children = [parse(c, n) for c, n in zip(contentsList, filenameList)]#, datesList + d
        return children

#output and input
@app.callback(Output('output', 'children'),
            Input('make_graph', 'n_clicks'),
            State('graph_choice', 'value'),
            State('store_id', 'data'),
            State('x_axis', 'value'),
            State('y_axis', 'value')) #State('color_choice', 'value'),
def graph_maker(n, chosen_graph, data, x_val, y_val): #, color
    if n is None:
        return dash.no_update
    #else:
        #fig = px.bar(data, x=x_val, y=y_val)
        #return dcc.Graph(figure=fig)
    elif chosen_graph == 'bar': #and color == 'Gold' or 'MediumTurquoise' or "LightGreen"
        fig = px.bar(data, x=x_val, y=y_val) #, marker_color=color
        return dcc.Graph(figure=fig)
    elif chosen_graph == 'map':
        fig2 = px.density_heatmap(data, x=x_val, y=y_val, marginal_x="histogram", marginal_y="histogram", text_auto=True)
        return dcc.Graph(figure=fig2)
    elif chosen_graph == 'scatter': #and color == 'red'
        fig3 = px.scatter(data, x=x_val, y=y_val) #, color="size" #, color="colors", color_continuous_scale=color
        return dcc.Graph(figure=fig3)
    #elif color == 'red':
        #fig4 = px.scatter(data, x=x_val, y=y_val) 
        #return dcc.Graph(figure=fig4)
    #elif chosen_graph == 'box':
        #fig5 = px.density_mapbox(data, lat='Latitude', lon='Longitude', z='Magnitude', radius=10,
                        #center=dict(lat=0, lon=180), zoom=0,
                        #mapbox_style="stamen-terrain")
        #fig5 = px.density_mapbox(data, x=x_val, y=y_val)
        #return dcc.Graph(figure=fig5)

    elif chosen_graph == 'analysis':
        #Histogram
        fig_hist = px.histogram(data, x=x_val, y=y_val)
        #Strip chart
        fig_strip = px.strip(data, x=x_val, y=y_val)
        #Sunburst
        #fig_sunburst = px.sunburst(data, x=x_val, y=y_val)
        fig_sunburst = px.sunburst(data, path=["x", "y", "timestamp"])
        #Empirical Cumulative Distribution
        fig_ecdf = px.ecdf(data, x=x_val, y=y_val)
        #Line chart
        fig_line = px.line(data, x=x_val, y=y_val)
        return [
        html.Div([
            html.Div([dcc.Graph(figure=fig_hist)], className="six columns"),
            html.Div([dcc.Graph(figure=fig_strip)], className="six columns"),
        ], className="row"),
        html.H2("Types", style={"textAlign":"center"}),
        html.Hr(),
        html.Div([
            html.Div([dcc.Graph(figure=fig_sunburst)], className="six columns"),
            html.Div([dcc.Graph(figure=fig_ecdf)], className="six columns"),
        ], className="row"),
        html.Div([
            html.Div([dcc.Graph(figure=fig_line)], className="twelve columns"),
        ], className="row"),
    ]
    elif chosen_graph == 'contour':
        fig1_contour = px.density_contour(data, x=x_val, y=y_val)
        fig2_contour = px.density_contour(data, x=x_val, y=y_val)
        fig2_contour.update_traces(contours_coloring="fill", contours_showlabels = True)
        #x1=x_val
        #y1=y_val
        #x1 = np.uniform(x_val) #np.random.uniform
        #y1 = np.uniform(y_val) 
        #fig3_contour = go.Figure(go.Histogram2dContour(x=x1, y=y1))
        #fig3_contour = go.Figure(go.Histogram2dContour(x=x_val, y=y_val))
        #
        #fig3_contour = px.density_contour(data, x=x_val, y=y_val, colorscale='Blues')
        #fig3_contour = px.density_contour(data, x=x_val, y=y_val, color='Blues')
        #
        fig3_contour = px.density_contour(data, x=x_val, y=y_val)
        fig3_contour.update_layout(template="plotly_white")
        fig3_contour.add_layout_image(
            dict(
                source="https://images.plot.ly/language-icons/api-home/python-logo.png",
                opacity=1,
                layer="below")
        )
        return [html.Div([ dcc.Graph(figure=fig1_contour),  dcc.Graph(figure=fig2_contour), dcc.Graph(figure=fig3_contour) ])]#, dcc.Graph(figure=fig3_contour)

#@app.callback(Output('output', 'children'), Input('type', 'value'))
#def make_graph(graph_chosen, contents, xVal):
    #string_content = contents.split(',')
    #decoder = base64.b64decode(string_content)
    #df = pd.read_csv(io.StringIO(decoder.decode('utf-8')))

    # HISTOGRAM
    #df_hist = df[df["type"]==graph_chosen]
    #fig_hist = px.histogram(df_hist, x=xVal)
    #fig_hist.update_xaxes(categoryorder="total descending")

if __name__ == '__main__':
    app.run_server(debug=True) #host='0.0.0.0' og port=8000
