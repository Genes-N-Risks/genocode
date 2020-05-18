import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.graph_objects as go

from app import app

import pandas as pd
import numpy as np

df1 = pd.read_csv('Polygenic Risk Scores Data.csv')

score = {}
for i in range(df1.shape[0]):
    if df1.phenotype[i] in score.keys():
        score[df1.phenotype[i]].append(df1.score[i])
    else:
        score[df1.phenotype[i]] = []
        score[df1.phenotype[i]].append(df1.score[i])
        
amean = {}
for i in range(df1.shape[0]):
    if df1.phenotype[i] in amean.keys():
        amean[df1.phenotype[i]].append(df1.means[i])
    else:
        amean[df1.phenotype[i]] = []
        amean[df1.phenotype[i]].append(df1.means[i])

astdev = {}
for i in range(df1.shape[0]):
    if df1.phenotype[i] in astdev.keys():
        astdev[df1.phenotype[i]].append(df1.sdev[i])
    else:
        astdev[df1.phenotype[i]] = []
        astdev[df1.phenotype[i]].append(df1.sdev[i])       
        
df = pd.read_csv('Genetic Data.csv')

options={'BMI':[],
         'T2D':[],
         'Glucose':[]}

for i in range(df.shape[0]):
    if df.gene[i] in options[df.phenotype[i]]:
        continue
    else:
        options[df.phenotype[i]].append(df.gene[i])
        
means = {}
for i in range(df.shape[0]):
    if df.gene[i] in means.keys():
        means[df.gene[i]].append(df.means[i])
    else:
        means[df.gene[i]] = []
        means[df.gene[i]].append(df.means[i])
        
stdevs = {}
for i in range(df.shape[0]):
    if df.gene[i] in stdevs.keys():
        stdevs[df.gene[i]].append(df.sdev[i])
    else:
        stdevs[df.gene[i]] = []
        stdevs[df.gene[i]].append(df.sdev[i])
        
genotype = {}
for i in range(df.shape[0]):
    if df.gene[i] in genotype.keys():
        genotype[df.gene[i]].append(df.genotype[i])
    else:
        genotype[df.gene[i]] = []
        genotype[df.gene[i]].append(df.genotype[i])

layout = html.Div([
    html.H3('Statistic data'),
    
    dcc.Dropdown(
        id='disease-dropdown',
        options=[{'label': k, 'value': k} for k in options.keys()],
        value = 'BMI'
    ),
    
    html.Hr(),
    
    dcc.Dropdown(id='snps-dropdown'),
    
    html.Hr(),
    
    
    html.Div(id='stat-display-value'),
    
    dcc.Link('Back to main page', href='main')
])


@app.callback(
    Output('snps-dropdown', 'options'),
    [Input('disease-dropdown', 'value')])
def set_snps_options(selected_disease):
    return [{'label': i, 'value': i} for i in options[selected_disease]]


@app.callback(
    Output('snps-dropdown', 'value'),
    [Input('snps-dropdown', 'options')])
def set_snps_value(available_options):
    return available_options[0]['value']


@app.callback(
    Output('stat-display-value', 'children'),
    [Input('disease-dropdown', 'value'),
     Input('snps-dropdown', 'value')])
def display_value(disease, snps):
    return [dcc.Graph(
        figure={
            'data':[
                {
                    'name': genotype[snps][0],
                    'type': 'violin',
                    'y': np.random.normal(means[snps][0], stdevs[snps][0], 1000)
                },
                
                {
                    'name': genotype[snps][1],
                    'type': 'violin',
                    'y': np.random.normal(means[snps][1], stdevs[snps][1], 1000)
                }, 
                                
                {
                    'name': genotype[snps][2],
                    'type': 'violin',
                    'y': np.random.normal(means[snps][2], stdevs[snps][2], 1000)
                }
            ],
            'layout': {
                'title': 'Violin plot of {} variants'.format(snps)
            }
        }
    ),
            
            dcc.Graph(
                figure=go.Figure(
                    go.Bar(
                            x=score[disease],
                            y=amean[disease],
                            error_y=dict(type='data', array=astdev[disease])
                    )
                    
                )
            )
           ]













