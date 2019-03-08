# -*- coding: utf-8 -*-
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
from dash.dependencies import Input, Output


external_stylesheets = ['/assets/style.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('mtcars.tsv', sep='\t')



mtcars_table = dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict("rows"),
        style_table={'overflowX': 'scroll'},
)

list_of_attributes = list(df.columns.values)
list_of_attributes.remove('model')

list_of_cars = list(df['model'])



#Layout of the App
app.layout = html.Div(children=[
    html.H1(children='Motor Trend Car Road Tests'),


    #View individual car statistics
    html.Div([
        html.H1(children='Select Your Ride'),
        dcc.Dropdown(
            id='input-model',
            options=[{'label': i, 'value': i} for i in df['model']],
            value='Mazda RX4',
        ),
    ]),

    #Radar plot of car
    dcc.Graph(id='plot_radar'),

    #Compare Car Attributes
    html.Div([
        html.H1(children='Compare Statistics of Various Car models'),
        dcc.Dropdown(
            id='input-attribute',
            options=[{'label': i, 'value': i} for i in list_of_attributes],
            value='mpg',
        ),
        dcc.Graph(id='plot-attribute'),
    ]),

    html.H2(children='Table of Car Models'),
    mtcars_table,

], style={'padding':64})


#Update Radar Plot based on Model Selected
@app.callback(
    dash.dependencies.Output('plot_radar', 'figure'),
    [Input(component_id='input-model', component_property='value')]
)
def update_output_div(input_value):
    car_index = list_of_cars.index(str(input_value))
    data_model = [go.Scatterpolar(
        r = [df['mpg'][car_index], df['qsec'][car_index] , df['wt'][car_index]*10, df['hp'][car_index]*0.1, df['disp'][car_index]*0.1],
        theta = ['Miles Per Gallon', 'Quarter Mile Time', 'Weight', 'Gross Horsepower', 'Displacement'],
        fill = 'toself'
    )]
    layout_model = go.Layout(
        polar = dict(
            radialaxis = dict(
                visible = True,
                range = [0, 55]
            )
        ),
        title=str(input_value)
    )
    return {
        'data': data_model, 
        'layout': layout_model   
    }




#Callback for model vs attribute plot
@app.callback(
    dash.dependencies.Output('plot-attribute', 'figure'),
    [Input(component_id='input-attribute', component_property='value')]
)
def update_output_div(input_value):
   return {
            'data': [
                go.Bar(
                    x=df['model'],
                    y=df[str(input_value)],
                    marker=go.bar.Marker(
                        color='rgb(0, 0, 255)'
                    )
                ),
            ],
            'layout': go.Layout(
                xaxis= {'title': 'Model',
                        'type': 'category'},
                yaxis={'title': str(input_value)},
                hovermode='closest'
            )
    }





if __name__ == '__main__':
    app.run_server(debug=True)