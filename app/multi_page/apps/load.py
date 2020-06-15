import base64
import datetime
import io

import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_table

import pandas as pd
import numpy as np
from scipy.stats import norm

from app import app

df_statistic = pd.read_csv('Genetic data.csv')
df_score = pd.read_csv('Polygenic Risk Scores Data.csv')

def search_bmi(df):
    array = ['rs9939609', 'rs6548238','rs17782313','rs10938397','rs7498665', 
             'rs10838738','rs11084753','rs2815752']
    df = df.loc[df['rsid'].isin(array)]
    return df 

def search_diabetes(df):
    array = ['rs560887','rs10830963','rs14607517','rs2191349','rs780094','rs11708067',
           'rs7944584','rs10885122','rs174550','rs11605924','rs11920090','rs7034200',
            'rs340874','rs11071657','rs13266634','rs7903146','rs35767']
    df = df.loc[df['rsid'].isin(array)]
    return df

def calculate_PGRS(df1,df2): #df1 refers to users data; df2 refers to dataset    
    size = []
    for i in range(len(df1)):
        row = df2[(df2['rsid'] == df1['rsid'][i]) 
                  & (df2['genotype'] == df1['genotype'][i])]
        size.append(row['effect'].values)
    PGRS = 0
    for i in range(len(size)):
        PGRS += size[i][0]
    return PGRS

def PGRS_contribution(df1,df2):
    contribution = {}
    for i in range(len(df1)):
        row = df2[(df2['rsid'] == df1['rsid'][i]) 
                  & (df2['genotype'] == df1['genotype'][i])]
        contribution[df1['rsid'][i]] = row['effect'].values[0]
    factor=1.0/sum(contribution.values())
    for k in contribution:
        contribution[k] = round(contribution[k]*factor,2)
    return contribution

def error_contribution(df1,df2):
    errors = {}
    for i in range(len(df1)):
        row = df2[(df2['rsid'] == df1['rsid'][i]) 
                  & (df2['genotype'] == df1['genotype'][i])]
        errors[df1['rsid'][i]] = row['effect_error'].values[0]/row['effect'].values[0]
    return errors

def get_BMI_statistic(score):
    if score <=3.5:
        return df_score['means'][0], df_score['sdev'][0]
    elif 3.5<score<=4.5:
        return df_score['means'][1], df_score['sdev'][1]
    elif 4.5<score<=5.5:
        return df_score['means'][2], df_score['sdev'][2]
    elif 5.5<score<=6.5:
        return df_score['means'][3], df_score['sdev'][3]
    elif 6.5<score<=7.5:
        return df_score['means'][4], df_score['sdev'][4]
    elif 7.5<score<=8.5:
        return df_score['means'][5], df_score['sdev'][5]
    elif 8.5<score<=9.5:
        return df_score['means'][6], df_score['sdev'][6]
    elif 9.5<score<=10.5:
        return df_score['means'][7], df_score['sdev'][7]
    elif 10.5<score<=11.5:
        return df_score['means'][8], df_score['sdev'][8]
    elif 11.5<score<=12.5:
        return df_score['means'][9], df_score['sdev'][9]
    else:
        return df_score['means'][10], df_score['sdev'][10] 

def get_T2D_statistic(score):
    if score <=12.5:
        return df_score['means'][11], df_score['sdev'][11]
    elif 12.5<score<=13.5:
        return df_score['means'][12], df_score['sdev'][12]
    elif 13.5<score<=14.5:
        return df_score['means'][13], df_score['sdev'][13]
    elif 14.5<score<=15.5:
        return df_score['means'][14], df_score['sdev'][14]
    elif 15.5<score<=16.5:
        return df_score['means'][15], df_score['sdev'][15]
    elif 16.5<score<=17.5:
        return df_score['means'][16], df_score['sdev'][16]
    elif 17.5<score<=18.5:
        return df_score['means'][17], df_score['sdev'][17]
    elif 18.5<score<=19.5:
        return df_score['means'][18], df_score['sdev'][18]
    elif 19.5<score<=20.5:
        return df_score['means'][19], df_score['sdev'][19]
    elif 20.5<score<=21.5:
        return df_score['means'][20], df_score['sdev'][20]
    elif 21.5<score<=22.5:
        return df_score['means'][21], df_score['sdev'][21]
    else:
        return df_score['means'][22], df_score['sdev'][22]
    
def solve(mu1,mu2,sigma1,sigma2):
    a = 1/(2*sigma1**2) - 1/(2*sigma2**2)
    b = mu2/(sigma2**2) - mu1/(sigma1**2)
    c = mu1**2 /(2*sigma1**2) - mu2**2 / (2*sigma2**2) - np.log(sigma2/sigma1)
    return np.roots([a,b,c])

def nordist_overlape(mu1, sigma1, mu2, sigma2):
    result = solve(mu1,mu2,sigma1,sigma2)
    r = result[0]
    area = norm.cdf(r,mu2,sigma2) + (1.-norm.cdf(r,mu1,sigma1))
    return area

rsid_genotype = {}  ## Dictionary where keys are rsid and values are genotype
for i in range(df_statistic.shape[0]):
    if df_statistic.rsid[i] in rsid_genotype.keys():
        continue
    else:
        rsid_genotype[df_statistic.rsid[i]] = []        
        rsid_genotype[df_statistic.rsid[i]].append(df_statistic.gene[i])  

layout = html.Div([
    html.H3('Please upload your 23&me txt file'),
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    html.Div(id='output-data-upload')
])


def parse_contents(contents, filename):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    
    if 'txt' in filename:
        # Now we only accept txt files
        df = pd.read_csv(
            io.StringIO(decoded.decode('utf-8')), '\s+', skiprows=20,
            names=['rsid','chromosome','position','genotype'])
        # replace all '--' with 'NaN'
        df = df.replace('--', 'NaN')
        global df_user 
        df_user = df  

@app.callback(Output('output-data-upload', 'children'),
              [Input('upload-data', 'contents')],
              [State('upload-data', 'filename')])
def update_output(list_of_contents, list_of_names):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n) for c, n in
            zip(list_of_contents, list_of_names)]        
        df_bmi = search_bmi(df_user)     
        df_bmi = df_bmi.reset_index(drop=True)   
        df_diabetes = search_diabetes(df_user)
        df_diabetes = df_diabetes.reset_index(drop=True)
        
        PGRS_bmi = calculate_PGRS(df_bmi, df_statistic)
        PGRS_bmi = round(PGRS_bmi/0.29*1.118056, 1)
        contribution_bmi = PGRS_contribution(df_bmi, df_statistic) 
        error_bmi = error_contribution(df_bmi, df_statistic) 
        
        genotype_bmi = []      ##convert rsid to fully genotype name
        for rsid in contribution_bmi.keys():
            genotype_bmi.append(rsid_genotype[rsid][0])
        
        PGRS_diabetes = calculate_PGRS(df_diabetes, df_statistic)
        PGRS_diabetes = round(PGRS_diabetes*1.2943, 1)  
        contribution_diabetes = PGRS_contribution(df_diabetes, df_statistic)
        error_diabetes = error_contribution(df_diabetes, df_statistic)
        
        genotype_diabetes = []      ##convert rsid to fully genotype name
        for rsid in contribution_diabetes.keys():
            genotype_diabetes.append(rsid_genotype[rsid][0])
        
        user_BMI_mean, user_BMI_stdev = get_BMI_statistic(PGRS_bmi)
        low_BMI_mean = df_score['means'][0]
        low_BMI_stdev = df_score['sdev'][0]
        BMI_overlap = nordist_overlape(low_BMI_mean, low_BMI_stdev, user_BMI_mean, user_BMI_stdev)
        BMI_risk = round((1-BMI_overlap)*100, 2)
        
        user_T2D_mean, user_T2D_stdev = get_T2D_statistic(PGRS_diabetes)
        low_T2D_mean = df_score['means'][11]
        low_T2D_stdev = df_score['sdev'][11]
        T2D_overlap = nordist_overlape(low_T2D_mean, low_T2D_stdev, user_T2D_mean, user_T2D_stdev)
        T2D_risk = round((1-T2D_overlap)*100, 2)
        
        return [html.H3('Your BMI polygenic risk score is {}'.format(PGRS_bmi)),
            dcc.Graph(
                figure={
                    'data':[
                        {
                        'x': list(genotype_bmi),
                        'type': 'bar',
                        'y': list(contribution_bmi.values()),
                        'error_y':{
                            'array':list(error_bmi.values()),
                            'type':'percent'
                        }
                        } 
                    ],
                    'layout': {
                        'title': 'Contributions of different SNPs to BMI Polygenic risk scores',
                    'yaxis':{
                        'title':'Contributions'
                    },
                    'xaxis':{
                        'title':'Genotypes'
                     }
                    }
                }
            ),
            html.H4('Compare with database, you have {}% risk of BMI issue'.format(BMI_risk)),
            html.Br(),
            html.Br(),
            html.Br(),
            html.H3('Your type II diabetes polygenic risk score is {}'.format(PGRS_diabetes)),
            dcc.Graph(
                figure={
                    'data':[
                        {
                        'x': list(genotype_diabetes),
                        'type': 'bar',
                        'y': list(contribution_diabetes.values()),
                        'error_y':{
                            'array':list(error_diabetes.values()),
                            'type':'percent'
                        }
                        } 
                    ],
                    'layout': {
                        'title': 'Contributions of different SNPs to type II diabetes Polygenic risk scores',
                    'yaxis':{
                        'title':'Contributions'
                    },
                    'xaxis':{
                        'title':'Genotypes'
                     }
                    }
                }
            ),
            html.H4('Compare with database, you have {}% risk of type II diabetes issue'.format(T2D_risk)),
        ] 
    else:
        return 'No content in upload file.'
    
        
 