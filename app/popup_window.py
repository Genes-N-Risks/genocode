import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div([
    dcc.ConfirmDialog(
        id='confirm',
        message='Consent form information / User can agree or disagree/ agree to contidue to the upload file page',
    ),

    dcc.Dropdown(
        options=[
            {'label': i, 'value': i}
            for i in ["Just browsing... I am not ready to upload my genetic result", 'sign the consent form / I want to upload my file and see the distribution']
        ],
        id='dropdown'
    ),
    html.Div(id='output-confirm')
])


@app.callback(Output('confirm', 'displayed'),
              [Input('dropdown', 'value')])
def display_confirm(value):
    if value == 'sign the consent form / I want to upload my file and see the distribution':
        return True
    return False


@app.callback(Output('output-confirm', 'children'),
              [Input('confirm', 'submit_n_clicks')])
def update_output(submit_n_clicks):
    if submit_n_clicks:
        return 'need to display the upload file webpage here.. how many times have users submitted their files {}'.format(submit_n_clicks)


if __name__ == '__main__':
    app.run_server(debug=True)
