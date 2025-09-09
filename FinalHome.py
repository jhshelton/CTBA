import dash 
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/")

layout = html.Div([
    html.H1("Industry Employment and Wages Dashboard"), 
    
    html.Div("This dashboard provides an overview of headcounts by industry in both a time series and a choropleth as well as wages by industry in a time series. The intended use is to be able to see impacts of historical events and trends on employment and wages within industries, how industries have moved around the nation over time, and to identify potential opportunities for historical research. See an explanation for the three pages below:", className="block block-top"),
    
    html.Div(
        html.Div(dbc.Card([dbc.CardHeader(html.A("Employee Headcount by Industry over Time", href="/FinalPage1", className= 'block', style = {'fontSize': '32px'})), dbc.CardBody('This page includes a time series of employee headcounts by industry over time. There is optionality to include whichever industries you are interested in using the checkboxes and a toggle to see a GDP-based recession indicator on a secondary axis.')]), className="block"),   
    ),
    
    html.Div(dbc.Card([dbc.CardHeader(html.A("Employee Headcount by Industry Map:", href="/FinalPage2", className= 'block', style = {'fontSize': '32px'})), dbc.CardBody('This page includes a choropleth based on employee headcounts for the specified industry. The data is available monthly, so both a year and month selector is included. Employee headcounts are presented as a percentage of total non-farm jobs within each state.')]), className="block"),  
    
    html.Div(dbc.Card([dbc.CardHeader(html.A("Average Hourly Wage By Industry Over Time:", href="/FinalPage3", className= 'block', style = {'fontSize': '32px'})), dbc.CardBody('This page includes a time series of average hourly wage within an industry over time. This hourly wage is specifically for production and non-supervisory roles because more data is available.')]), className="block"),
    html.Small("Jackson Shelton, Justin Varela, Pranav Prathap, Yixuan Tan", className="footer-small")
])

