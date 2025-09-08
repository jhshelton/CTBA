from dash import Dash, Input, Output, html, dcc, callback
import dash_bootstrap_components as dbc
import plotly_express as px
import pandas as pd
import numpy as np
import json
from datetime import datetime
import requests
import datetime


url = 'https://api.stlouisfed.org/fred/series/observations'
fred_api_key = '1d90de899e9698a2924f22d85c093fe6'
series_identifiers = ['USMINE', 'USCONS', 'MANEMP', 'DMANEMP', 'NDMANEMP', 'USWTRADE', 'USTRADE', 'CES4300000001','CES4422000001','USINFO', 'USFIRE', 'USPBS', 'USEHS', 'USLAH', 'USSERV', 'USGOVT']
series_labels = ['Mining and Logging', 'Construction', 'Manufacturing', 'Durable Goods', 'Nondurable Goods', 'Wholesale Trade', 'Retail Trade', 'Transportation and Warehousing', 'Utilities', 'Information', 'Financial Activities', 'Professional and Business Services', 'Education and Health Services', 'Leisure and Hospitality', 'Other Services', 'Government']

df = pd.DataFrame(columns = ['realtime_start', 'realtime_end', 'date', 'value', 'id'])

for i in range(len(series_identifiers)):
    
    params = {
    'series_id': series_identifiers[i],
    'api_key': fred_api_key,
    'file_type':'json'
    }
    
    response = requests.get(url, params = params)
    if response.status_code == 200:
        data = response.json()
        obs = data.get('observations', [])
        dftemp = pd.DataFrame(obs)
        dftemp['id'] = series_labels[i]
        dftemp['value'] = pd.to_numeric(dftemp['value'], errors = 'coerce')
        dftemp['date'] = pd.to_datetime(dftemp['date'], errors = 'coerce')
        frame = [df, dftemp]
        df = pd.concat(frame)



app = Dash(__name__)
app.title = 'Industry Employment Statistics'

#controls
controls = html.Div([
    html.Div('Select Industries to Chart'),
    dcc.Checklist(
        options = [
            {'label': industry, 'value': industry} for industry in series_labels
        ],
        id = 'checklist'
    )
])

Test_output = dcc.Graph(id = 'checkout')

date_control = dcc.DatePickerRange(id = 'daterange',
                                   start_date = datetime.datetime(year = 1960, month = 1, day = 1),
                                   end_date = datetime.date.today())

app.layout = html.Div([
    controls,
    Test_output,
    date_control,
 
    
])

@app.callback(
    Output('checkout', 'figure'),
 
    Input('checklist', 'value'),
    Input('daterange', 'start_date'),
    Input('daterange','end_date')
)
def update(industries, start, end):
    
    filtered_df = df[df['id'].isin(industries)]
    filtered_df = filtered_df[filtered_df['date']<= end]
    filtered_df = filtered_df[filtered_df['date']>= start]
    fig = px.line(filtered_df, x = 'date', y= 'value', color = 'id')
    return fig

if __name__ == '__main__':
    app.run()