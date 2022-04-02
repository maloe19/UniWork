#import matplotlib #https://matplotlib.org/stable/api/index

#---------------------------------------------------------

#https://plotly.com/python/getting-started/
#https://dash.plotly.com/layout

#------------------------------
#import plotly.express as px
#from dash import Dash, html, Input, dcc
#import pandas as pd

#fig = px.bar(x=["a","b","c"], y=[3, 2, 1])
#fig.write_html('first_figure.html', auto_open=True)
#---------------------------------------------------

#app  = Dash(__name__)

#app.layout = html.Div([
    #htl elements
        #dcc.Upload(
        #id='upload-id',
        #children=html.Div([
            #'Upload file'
        #]),
        #style={

        #},
        ##Uploading multiple files is allowed
        #multiple=True
        #), 
#])

#@app.callback(
    #output and input
#)

#def display():
    ##simplest form:
        #fig = px.bar(x=["a","b","c"], y=[3, 2, 1])
        #fig.show()
    #return figure

#if __name__ == '__main__':
    #app.run_server(debug=True)

#rester
    #excel reading
        #if 'xls' in filename:
            #fina = pd.read_excel(io.BytesIO(dcode))

    #forsøg 1 på visualisering
            #return html.Div([
        #html.H5(filename),
        
        #dcc.Graph(
            #fina.to_dict('records'),
            #[{'name': i, 'id': i} for i in fina.columms]
        #)
        #])