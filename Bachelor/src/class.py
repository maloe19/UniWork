import plotly.express as px
from dash import Dash, html, Input, dcc, Output, State
import pandas as pd
import io
import base64

#fig = px.bar(x=["a","b","c"], y=[3, 2, 1])
#fig.write_html('first_figure.html', auto_open=True)

app  = Dash(__name__)

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
        id='input',
        children=html.Div([
            html.Button('Upload file')
        ]),
    ),
    html.Hr(),
    html.Div(id='output'),
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
    return html.Div([
        html.H5(filename),
        
        dcc.Graph(
            fina.to_dict('records'),
            [{'name': i, 'id': i} for i in fina.columms]
        )
    ])

@app.callback(
    Output('output', 'children'),
    Input('input', 'content'),
    State('input', 'filename')
)

def update(contentList, filenameList):
    if contentList is not None:
        children = [
            parse(cL, fnL) for cL, fnL in zip(contentList, filenameList)
        ]
        return children

#def colorMethod(color):
    #viz = reference til px.bar i parse methode
     #og så brug markColor=color

if __name__ == '__main__':
    app.run_server(debug=True)
