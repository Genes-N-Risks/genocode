import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

layout = html.Div([
    html.H1("Welcome to Genocode"),
    html.H2("Dear users, Gene 'n Risk provide you will personalliezed service of disease risk analysis!"),
    dcc.Link('Check more details about genes and risks', href='/statistic'),
])