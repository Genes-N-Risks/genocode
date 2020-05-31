import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

layout = html.Div([
    html.H1("Welcome to Genocode"),
    html.H2("Genocode is a data visualization tool designed to help you understand the actual risk of diseases posed by your genetics! Customers of DNA testing services (Currently only 23andMe) use Genocode to learn more about their DNA variants."),
    html.H3("Please sign the consent form in order to get your own personalized disease risk assessment."),
    dcc.Link('Sign the consent form here', href='/consent'),
    html.Br(),
    html.H3("At Genocode, we believe in 100% transparency. To learn more about the statistical data which we use to identify and assess your risks, please click 'Statistic data of different diseases'"),
    dcc.Link('Statistic data of different diseases', href='/statistic'),
])
