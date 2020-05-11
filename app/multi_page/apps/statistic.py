import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

layout = html.Div([
    html.H3('Statistic data'),
    dcc.Dropdown(
        id='stat-dropdown',
        options=[
            {'label': '{}'.format(i), 'value': i} for i in [
                'BMI', 'Type 2 diabetes', 'Fasting blood glucose'
            ]
        ]
    ),
    html.Div(id='stat-display-value'),
    dcc.Link('Back to main page', href='main')
])


@app.callback(
    Output('stat-display-value', 'children'),
    [Input('stat-dropdown', 'value')])
def display_value(value):
    return ['You have selected "{}"'.format(value),
           html.H4('Plot will be displayed here')]