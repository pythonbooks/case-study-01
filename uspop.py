# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import process

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
#    html.H1(children='Hello Dash'),

#    html.Div(children='''
#        Dash: A web application framework for Python.
#    '''),
    html.Div(
        dcc.Graph(
            id='bar-graph',
            figure=process.get_bar()
        )
    ),
        
    html.Div(
        dcc.Graph(
            id='cmap-graph',
            figure=process.get_cmap()
        )
    )
    
])

if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port=8080, debug=True)