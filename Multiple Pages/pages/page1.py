import dash
from dash import html

dash.register_page(__name__, path = '/page1', name = 'page 1')

layout = html.Div([
    html.Div('Top Row: with 1 Column', className = 'block block-top'),
    
    #Middle 2 Column
    html.Div([
        html.Div('Middle Left', className='block'),
        html.Div('Middle Right', className = 'block')
    ], className= 'row-2'),
    
    #footer
    html.Div('Footer', className ='block block-footer') #internal style takes precedence over external
    
    
    
], className='page1-grid')