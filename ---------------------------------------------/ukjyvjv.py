import dash 
import dash_core_components as dcc 
import dash_html_components as html 

import plotly.express as px
import plotly.graph_objs as go 

from dash.dependencies import Input, Output


df = px.data.gapminder()
all_continent = df.continent.unique()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        dcc.Checklist(
            id='continent_selected',
            options=[
                {'label':k, 'value':k}
                for k in all_continent
            ],
            labelStyle={'display': 'inline-block', 'color':'white'}
        ),
        dcc.Graph(id='graphic')
    ]
)

@app.callback(Output('graphic', 'figure'),
              [Input('continent_selected', 'value')])
def update_figure(continent):
    frame = df[df.continent == continent]
    
    fig = px.line(frame, x='year', y='lifeExp')

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)