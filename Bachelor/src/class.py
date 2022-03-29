import plotly.express as px
from dash import Dash, html, Input, dcc
import pandas as pd
import io

#fig = px.bar(x=["a","b","c"], y=[3, 2, 1])
#fig.write_html('first_figure.html', auto_open=True)

app.layout = html.Div([
    dcc.Upload(html.Button('Upload file')),
    html.Hr(),
    html.Div(id='output'),
])

def parse():
    return

@app.callback(

)

def update():
    return

    
