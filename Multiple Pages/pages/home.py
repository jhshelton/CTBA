import dash
from dash import html

dash.register_page(__name__, path = '/')

layout = html.Div([
    html.H2('Welcome to the home page'),
    html.P("this is a simple multi-page dash project")
    
    
    
])