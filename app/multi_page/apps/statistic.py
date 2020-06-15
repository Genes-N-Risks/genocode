import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.graph_objects as go

from app import app

import pandas as pd
import numpy as np
import scipy.stats as stats
from scipy.stats import norm
from statistics import NormalDist

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
         'T2D':[]}

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

xlabel = {'BMI':'Obesity Genetic Score', 'T2D':'Glucose Genetic Score'}
ylabel = {'BMI':'BMI(kg/m2)', 'T2D':'Fasting glucose(mg/dl)'}

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
    
    dcc.Link('Upload my 23&me file to get a personal analysis of my risk diesease', href='load')
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
    x1 = np.linspace(means[snps][0] - 3*stdevs[snps][0], means[snps][0] + 3*stdevs[snps][0], 100)
    x2 = np.linspace(means[snps][1] - 3*stdevs[snps][1], means[snps][1] + 3*stdevs[snps][1], 100)
    x3 = np.linspace(means[snps][2] - 3*stdevs[snps][2], means[snps][2] + 3*stdevs[snps][2], 100)
    ol1 = 100*NormalDist(means[snps][0], stdevs[snps][0]).overlap(NormalDist(means[snps][1], stdevs[snps][1]))
    ol1 = round(ol1,1)
    ol2 = 100*NormalDist(means[snps][0], stdevs[snps][0]).overlap(NormalDist(means[snps][2], stdevs[snps][2]))
    ol2 = round(ol2,1)
    return [dcc.Graph(
            figure={
                'data':[
                    {
                        'name': genotype[snps][0],
                        'type': 'line',
                        'x': x1,
                        'y': stats.norm.pdf(x1,means[snps][0], stdevs[snps][0])
                    },

                    {
                        'name': genotype[snps][1],
                        'type': 'line',
                        'x': x2,
                        'y': stats.norm.pdf(x2,means[snps][1], stdevs[snps][1])
                    }, 

                    {
                        'name': genotype[snps][2],
                        'type': 'line',
                        'x': x3,
                        'y': stats.norm.pdf(x3,means[snps][2], stdevs[snps][2])
                    }
                ],
                'layout': {
                    'title': 'Violin plot of {} variants'.format(snps),
                    'yaxis':{
                        'title':'Density'
                    },
                    'xaxis':{
                        'title':'Polygenic Risk Score'
                     }
                }
            }
        ),  
        html.H4('Overlap of single mutation {} and wild type {} is {}%'.format(genotype[snps][1],genotype[snps][0],ol1)), 
        html.H4('Overlap of double mutation {} and wild type {} is {}%'.format(genotype[snps][2],genotype[snps][0],ol2)),
        html.Br(),
        dcc.Graph(
            figure={
                'data':[
                    {
                        'name': score[disease][k]+'',
                        'type': 'violin',
                        'y': np.random.normal(amean[disease][k], astdev[disease][k], 1000)
                    } for k in range(len(score[disease]))
                ],
                'layout': {
                    'title': 'Polygenic risk scores distributuion of {}'.format(disease),
                    'yaxis':{
                        'title':ylabel[disease]
                    },
                    'xaxis':{
                        'title':xlabel[disease]
                     }
                }
            }
        )
               ]













