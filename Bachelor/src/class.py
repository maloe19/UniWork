import plotly.express as px
from dash import Dash, html, dcc, Input, Output, State, dash_table
import pandas as pd
import io
import base64
import dash

app  = Dash(__name__, suppress_callback_exceptions=True) 

app.layout = html.Div([
    dcc.Upload(
        id='dataUpload',
        children=html.Div([
            html.Button('Upload file')
        ]),
    ),
    html.Hr(),
    html.Div(id='output'),
    html.Div(id='outputTable'),
])

def parse(contents, filename):
    string = contents.split(',')
    dcode = base64.b64decode(string)
    try:
        if 'csv' in filename:
            fina = pd.read_csv(io.StringIO(dcode.decode('utf-8')))
    except Exception as e:
        print(e)
        return html.Div(['Something went wrong'])
    return html.Div([
        html.P("Pick x-axis"),
        dcc.Dropdown(id='xAxis', options=[{'label':x, 'value':x} for x in fina.columns]),
        html.P("Pick y-axis"),
        dcc.Dropdown(id='yAxis', options=[{'label':x, 'value':x} for x in fina.columns]),
        html.Button(id='makeGraph', children="Make Graph"),
        html.Hr(),
        dash_table.DataTable(
            info=fina.to_dict('records'),
            columns=[{'name': i, 'id': i} for i in fina.columns],
        ),
        dcc.Store(id='storeID', info=fina.to_dict('records')),
    ])

@app.callback(
    Output('outputTable', 'children'),
    Input('dataUpload', 'contents'),
    State('dataUpload', 'filename'),
    #State('dataUpload', 'modify'),
)
def update(contents, filename): 
    if contents is not None:
        children = [parse(ct, fn) for ct, fn in zip(contents, filename)]
    return children

@app.callback(
    Output('output', 'children'),
    Input('makeGraph', 'button'),
    State('storeID', 'info'),
    State('xAxis', 'value'),
    State('yAxis', 'value'),
)
def graphMaker(xValues, yValues, data, n): 
    if n is None:
        return dash.no_update
    else:
        fig = px.bar(data, x=xValues, y=yValues)
        return dcc.Graph(figure=fig)

if __name__ == '__main__':
    app.run_server(debug=True) #host='0.0.0.0' og port=8000
