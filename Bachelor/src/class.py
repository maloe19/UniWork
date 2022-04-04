#import plotly.express as px
from dash import Dash, html, dcc, Input, Output
import pandas as pd
import io
import base64
import plotly.graph_objs as go

#from dash.dependencies import Input, Output
#import dash_core_components as dcc

app  = Dash(__name__)

#variabel: colors

app.layout = html.Div([
    #drop-down med farver
    dcc.Dropdown(
        id="dropdown",
        options=['blue', 'red', 'yellow'],
        value='blue',
        #flere properties
    ),
    html.Hr(),
    dcc.Upload(
        id='dataUpload',
        children=html.Div([
            html.Button('Upload file')
        ]),
    ),
    html.Hr(),
    dcc.Graph(id='graphId')
])

def parse(contents, filename):
    string = contents.split(',')
    dcode = base64.b64decode(string)
    try:
        if 'csv' in filename:
            fina = pd.read_csv(io.StringIO(dcode.decode('utf-8')))
        elif 'xls' in filename:
            fina = pd.read_excel(io.BytesIO(dcode))
        elif 'txt' or 'tsv' in filename:
            fina = pd.read_csv(io.StringIO(dcode.decode('utf-8')), delimiter = r'\s+')
    except Exception as e:
        print(e)
        return html.Div(['Something went wrong'])
        
    return fina


@app.callback(
    Output('graphId', 'figure'),
    [
        Input('dataUpload', 'contents'),
        Input('dataUpload', 'filename')
    ]
)

def graphUpdate(contents, filename):
    fig = {
        'layout': go.Layout(
            #colors
        )}
    if contents:
        contents = contents[0]
        filename = filename[0]
        fina = parse(contents, filename)
        fina = fina.set_index(fina.columns[0])
        fig['data'] = fina.iplot(asFigure=True, kind='scatter', mode='lines+markers', size=1)
    return fig

#def colorMethod(color):
    #viz = reference til px.bar i parse methode
     #og så brug markColor=color

if __name__ == '__main__':
    app.run_server(debug=True) #host='0.0.0.0' og port=8000
