#Import required libraries
import datetime
import yfinance as yf
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

#Create a user interface using the dash library

# We are going to make a simple yet functional user interface, one will be a simple Heading title and an input textbox for the user to type in the stock names.
app = dash.Dash()
app.title = "Stock Visualization"
app.layout - html.Div(children=[
    html.H1("Stock Visualization Dashboard"),
    html.H4("Please enter the stock name"),
    dcc.Input(id='input', value='AAPL', type='text'),
    html.Div(id='output-graph')
])

#Add an app call back to get input data
# The input text box is now just a static text box. To get the input data, which in this case is the stock name of a company, from the user interface, 
# we should add app callbacks.  The read stock name(input_data) is passed as a parameter to the method update_value. The function then gets all the stock
# data from the Yahoo Finance API from 1st January 2010 till now, the current day, and is stored in a Pandas data frame. A graph is plotted, with the X-axis
# being the index of the data frame, which is time in years, the Y-axis with the closing stock price of each day, and the name of the graph being the stock 
# name(input_data). This graph is returned to the callback wrapper which then displays it on the user interface.

#callback Decorator
@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='input', component_property='value')]
)

def update_graph(input_data):
    start = datetime.datetime(2010, 1, 1)
    end = datetime.datetime.now()

    try:
        df = web.Datareader(input_data, 'yahoo', start, end)

        graph = dcc.Graph(id = "example", figure ={
            'data':[{'x':df.index, 'y':df.Close, 'type':'line', 'name':input_data}],
            'layout':{
                'title':input_data
            }
        }
        )
    except:
        graph = html.Div("Error retrieving stock data.")

    return graph

#Run the server
if __name__ == '__main__':
    app.run_server()
