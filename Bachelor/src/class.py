#import plotly.express as px
from dash import Dash, html, Input, dcc, Output
import pandas as pd
import io
import base64
import plotly.graph_objs as go

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
        id='upload',
        children=html.Div([
            html.Button('Upload file')
        ]),
    ),
    html.Hr(),
    dcc.Graph(id='graphId')
])

def parse(content, filename):
    string = content.split(',')
    dcode = base64.b64decode(string)
    try:
        if 'csv' in filename:
            fina = pd.read_csv(io.StringIO(dcode.decode('utf-8')))
    except Exception as error:
        print(error)
        return html.Div(['Something went wrong'])
    return fina


@app.callback(
    Output('graphId', 'figure'),
    [
        Input('upload', 'content'),
        Input('upload', 'filename')
    ]
)

def graphUpdate(content, filename):
    fig = {
        'layout': go.Layout(
            #colors
        )}
    if content:
        content = content[0]
        filename = filename[0]
        fina = parse(content, filename)
        fina = fina.set_index(fina.columns[0])
        fig['data'] = fina.iplot(asFigure=True, kind='scatter', mode='lines+makers', size=1)
    return fig

#def colorMethod(color):
    #viz = reference til px.bar i parse methode
     #og så brug markColor=color

if __name__ == '__main__':
    app.run_server(debug=True)
