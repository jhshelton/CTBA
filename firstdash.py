
from dash import Dash, html
#dash is built on plotly, Flask, and React
#made for static and dynamic dashboards
#plotly is for individual graphs instead of a full dashboard
#matplotlib is for static plots
#dash is dynamic in that it responds to user input, databse queries, api calls, or changes in real time to the data stream
#callbacks: functions decorated with @app.callback() listen for changes in user inputs and update outputs dynamically
#dash builds HTML pages at runtime
#can handle: APIs, Databases, and live data streams

app = Dash(__name__)

#recall: HTML is broken into headings and paragraphs, headings are numbered for size not order, paragraphs are not numbered.
#html.div means division, as in a separator between elements
#anchor adds hyperlinks to other pages
#br is a line break
# define the layout
app.layout = html.Div([html.H1('Hello Dash', style = {'color': '#381D5C', 
                                                      'fontSize' :'20px', 
                                                      'backgroundColor' : '#E898AA'}), 
                       html.P('This is a simple Dashboard', style = {'border':'1px solid black',
                                                                     'borderradius':'10px',
                                                                     'padding':'20px',
                                                                     'margin':'50px'}), 
                       html.Br(), 
                       html.A("click here", href = 'https://example.com')])

#set the title
app.title= 'My First Dash App'

#run the app (it will give you a link in the command line)
if __name__ == '__main__':
    app.run(debug = True, use_reloader = False)