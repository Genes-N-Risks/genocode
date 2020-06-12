import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

layout = html.Div([
    html.H1('Terms of service'),
    #html.H3('Name'),
    #dcc.Input(id='input-1-state', value='Name', type='text'),
    # html.H3('gender'),
    # dcc.Input(id='input-2-state', value='Male/Female', type='text'),
    # html.H3('birthday'),
    # dcc.Input(id='input-3-state', value='MM/DD/YY', type='text'),
    # html.Div(id="constent_page"),
    dcc.Markdown(
    '''
**GenoCode will not collect or use any data from users. ** Your genetic test file will be analyzed on the website and you need to save the given risk result for your own use. Once you close the website, you need to upload the file again to see the result. If you have questions, concerns, complaints, or suggestions about our website, you can reach out to us via email.
'''
    ),
    html.Br(),
    html.Br(),
    html.Br(),
    dcc.Link('I have read the above information.', href='load'),
    html.Br(),
    dcc.Link('Back to main page', href='main')
])





