import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

layout = html.Div([
    html.H1("Welcome to Gene 'n Risk"),
    html.H2("Dear users, Gene 'n Risk provide you will personalliezed service of disease risk analysis!"),
    html.H3(" Please click 'Sign in my consent form', to signup a consent form of yourself and upload your SNPs test result to get your personallized disease risk analysis"),
    html.H3(" Please click 'Just go through statistic data of differnt disease', to look up statistic data"),
    dcc.Link('Sign in my consent form', href='/consent'),
    html.Br(),
    dcc.Link('Just go through statistic data of differnt disease', href='/statistic'),
])