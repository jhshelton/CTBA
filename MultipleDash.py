from dash import Dash, html, dcc, Input, Output, callback

#initialize the app
app = Dash(__name__)

app.layout = html.Div([
    dcc.Input(id = 'input1', type = 'number', placeholder = 'Enter a number'),
    dcc.Input(id = 'input2', type = 'number', placeholder = 'Enter another number'),
    dcc.Input(id = 'input3', type = 'text', placeholder = 'enter some text'),
    
    html.Div(id = 'output1'),
    html.Div(id = 'output2'),
    html.Div(id = 'output3')
    
    
    
])
@app.callback(
    Output('output1', 'children'),
    Output('output2','children'),
    Output('output3','children'),
    
    Input('input1', 'value'),
    Input('input2', 'value'),
    Input('input3', 'value')        
)

def update_outputs(num1, num2, sentence):
    #handle none values to avoid errors
    num1 = num1 or 0
    num2 = num2 or 0
    sentence = sentence or ""
    
    #perform operations
    result1 = f'The Sum of the first two numbers is {num1+num2}'
    result2 = f'the Product of the first two numbers is {num1 *num2}'
    result3 = f'the reversed text of the third cell is {sentence[::-1]}'

    return result1, result2, result3


app.run(debug = True)