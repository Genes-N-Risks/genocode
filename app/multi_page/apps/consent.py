import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

layout = html.Div([
    html.H1('Users consent form'),
    html.H3('name'),
    dcc.Input(id='input-1-state', value='Name', type='text'),
    html.H3('gender'),
    dcc.Input(id='input-2-state', value='Male/Female', type='text'),
    html.H3('birthday'),
    dcc.Input(id='input-3-state', value='MM/DD/YY', type='text'),
    html.Div(id="constent_page"),
    html.Br(),
    html.Br(),
    html.Br(),
    dcc.Link('Submit', href='load'),
    html.Br(),
    dcc.Link('Back to main page', href='main')
])





