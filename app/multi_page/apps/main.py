import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app


layout = html.Div([
    html.H1(children = "Welcome to Genocode !",
            style = {
                'textAlign' : 'center',
                'color' : '#526753'
            }
            ),
    
    dcc.Markdown(
    '''
What if we told you that understanding your own genetic data can SAVE YOUR LIFE? 
Well we’re here to tell you that it can! We present to you **GENOCODE**! An app that allows you to privately and better understand genetic variations in your DNA associated with common diseases and health conditions. 
With a market worth of around $1B, current genetic services like *23andMe* [Visit 23andMe](https://www.23andme.com/) incompletely describe the true risk of your results being associated with a particular outcome. THAT’S YOUR LIFE ON THE LINE!
'''
    ),
    dcc.Markdown(
    '''
With GenoCode, you will be able to privately upload your genetic test results from common genetic services to our app, see your genetic data come to life, and be given a true risk evaluation for a given disease or health condition. GenoCode will be the only product to describe population variability depending on variables, such as your age, gender, and ethnicity. It is simple, accurate, and free! Get ready to become an expert in your own genetics.
'''
    ),        
    dcc.Link('Check more details about genes and risks', href='statistic'),
    html.Br(),
    html.Br(),
    dcc.Link('Upload my file', href='/consent'),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.A([
            html.Img(
                src='https://s3-us-west-2.amazonaws.com/uw-s3-cdn/wp-content/uploads/sites/98/2014/10/07214216/Signature_Left_Purple_RGB.png',
                style={
                    'height' : '60%',
                    'width' : '60%',
                    'float' : 'left',
                    'position' : 'relative',
                    'padding-top' : 0,
                    'padding-right' : 0
                })
    ], href='https://s3-us-west-2.amazonaws.com/uw-s3-cdn/wp-content/uploads/sites/98/2014/10/07214216/Signature_Left_Purple_RGB.png')
])