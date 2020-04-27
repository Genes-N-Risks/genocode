import base64
import datetime
import io

import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_table

import pandas as pd


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
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
    html.Div(id='output-data-upload'),
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
    else:
        return html.Div([
            'There was an error in file type. Please upload your txt file'
        ])

    return html.Div([
        html.H5('Filename is: {}'.format(filename)),
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'name': i, 'id': i} for i in df.columns]
        )
    ])


@app.callback(Output('output-data-upload', 'children'),
              [Input('upload-data', 'contents')],
              [State('upload-data', 'filename')])
def update_output(list_of_contents, list_of_names):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n) for c, n in
            zip(list_of_contents, list_of_names)]
        return children
    else:
        return 'Not content in upload file.'



if __name__ == '__main__':
    app.run_server(debug=True)