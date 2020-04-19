"""
This is the web tool to visualize normal distributions and calcualted overlape.
Users need to input mean and stdev of normal distributions.
This web tool is developed using dash.
Before run this file, pelase import Dash packages. 
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import numpy as np
import scipy.stats as stats
from scipy.stats import norm

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Input(id='input1',value=None, type='number', placeholder='mean of SNP1'),
    dcc.Input(id='input2',value=None, type='number', placeholder='stdev of SNP1'),
    dcc.Input(id='input3',value=None, type='number', placeholder='mean of SNP2'),
    dcc.Input(id='input4',value=None, type='number', placeholder='stdev of SNP2'),
    dcc.Input(id='input5',value=None, type='number', placeholder='mean of SNP3'),
    dcc.Input(id='input6',value=None, type='number', placeholder='stdev of SNP3'),
    html.Button(id='submit-button-state', n_clicks=0, children='Submit'),
    html.Div(id='output')
])

def solve(mu1,mu2,sigma1,sigma2):
    
    """
    This function calculates intercept of two normal distribution curvers.
    """
    a = 1/(2*sigma1**2) - 1/(2*sigma2**2)
    b = mu2/(sigma2**2) - mu1/(sigma1**2)
    c = mu1**2 /(2*sigma1**2) - mu2**2 / (2*sigma2**2) - np.log(sigma2/sigma1)
    return np.roots([a,b,c])

def nordist_overlape(mu1, sigma1, mu2, sigma2):
    """
    This function calculates overlape percentage of two normal distribution curvers.
    """
    result = solve(mu1,mu2,sigma1,sigma2)
    r = result[0]
    if mu1<mu2:
        area = 100*(norm.cdf(r,mu2,sigma2) + (1.-norm.cdf(r,mu1,sigma1)))
    elif mu1 == mu2:
        area = 100
    else:
        area = 100*(1.-norm.cdf(r,mu2,sigma2) + norm.cdf(r,mu1,sigma1))
    return area

@app.callback(
    Output('output', 'children'),
    [Input('submit-button-state', 'n_clicks')],
    [State('input1', 'value'),
     State('input2', 'value'),
     State('input3', 'value'),
     State('input4', 'value'),
     State('input5', 'value'),
     State('input6', 'value')])
def update_output(n_clicks, input1, input2, input3, input4, input5, input6):
    if input1 == input2 == input3 == input4 == input5 == input6 == None:
        return '''Waiting for input value from user to generate plots'''
    else:
        mu1 = input1
        sigma1 = input2
        mu2 = input3
        sigma2 = input4
        mu3 = input5
        sigma3 = input6
        ol1 = nordist_overlape(mu1, sigma1, mu2, sigma2)
        ol2 = nordist_overlape(mu1, sigma1, mu3, sigma3)
        x1 = np.linspace(mu1 - 3*sigma1, mu1 + 3*sigma1, 100)
        x2 = np.linspace(mu2 - 3*sigma2, mu2 + 3*sigma2, 100)
        x3 = np.linspace(mu3 - 3*sigma3, mu3 + 3*sigma3, 100)
        return [dcc.Graph(
            id='example-graph',
            figure={
                'data': [
                    {'x': x1, 'y': stats.norm.pdf(x1, mu1, sigma1), 'type': 'line','name': 'SNP1'},
                    {'x': x2, 'y': stats.norm.pdf(x2, mu2, sigma2), 'type': 'line','name': 'SNP2'},
                    {'x': x3, 'y': stats.norm.pdf(x3, mu3, sigma3), 'type': 'line','name': 'SNP3'},
                ],
                'layout': {
                    'title': 'Distribution of SNPs'
                }
            }
        ),
               html.H6('Overlape of SNP1 and SNP2 is {0:.2f}%'.format(ol1)),
               html.H6('Overlape of SNP1 and SNP3 is {0:.2f}%'.format(ol2))]
if __name__ == '__main__':
    app.run_server(debug=True)