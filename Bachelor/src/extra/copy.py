from dash import Dash, dcc, html, Input, Output
import plotly.express as px

app = Dash(__name__)


app.layout = html.Div([
    html.H4("Interactive color mode option with Dash"),
    html.P("Color mode:"),
    dcc.RadioItems(
        id='color-mode', 
        value='discrete', 
        options=['discrete', 'continuous'],
    ),
    dcc.Graph(id="graph"),
])


@app.callback(
    Output("graph", "figure"), 
    Input("color-mode", "value"))
def generate_chart(mode):
    df = px.data.tips() # replace with your own data source
    if mode == 'discrete':
        df["size"] = df["size"].astype(str)
    else:
        df["size"] = df["size"].astype(float)

    fig = px.scatter(
        df, x="total_bill", y="tip", color="size",
        title=f"'size' values mean using {mode.upper()} colors")
    return fig

app.run_server(debug=True)

############################

#from dash import Dash, dcc, html, Input, Output
#import plotly.express as px

#colorscales = px.colors.named_colorscales()

#app = Dash(__name__)


#app.layout = html.Div([
    #html.H4('Interactive color scale'),
    #html.P("Select your palette:"),
    #dcc.Dropdown(
        #id='dropdown', 
        #options=colorscales,
        #value='viridis'
    #),
    #dcc.Graph(id="graph"),
#])


#@app.callback(
    #Output("graph", "figure"), 
    #Input("dropdown", "value"))
#def change_colorscale(scale):
    #df = px.data.iris() # replace with your own data source
    #fig = px.scatter(
        #df, x="sepal_width", y="sepal_length", 
        #color="sepal_length", color_continuous_scale=scale)
    #return fig


#app.run_server(debug=True)

#############################

#from dash import Dash, dcc, html, Input, Output
#import plotly.graph_objects as go

#app = Dash(__name__)


#app.layout = html.Div([
    #html.H4('Interactive color selection with simple Dash example'),
    #html.P("Select color:"),
    #dcc.Dropdown(
        #id="dropdown",
        #options=['Gold', 'MediumTurquoise', 'LightGreen'],
        #value='Gold',
        #clearable=False,
    #),
    #dcc.Graph(id="graph"),
#])


#@app.callback(
    #Output("graph", "figure"), 
    #Input("dropdown", "value"))
#def display_color(color):
    #fig = go.Figure(
        #data=go.Bar(y=[2, 3, 1], # replace with your own data source
                    #marker_color=color))
    #return fig


#app.run_server(debug=True)