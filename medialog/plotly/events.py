from plone import api
from zope.i18nmessageid import MessageFactory

#plotly stuff
import plotly 
from plotly.graph_objs import Bar, Scatter, Figure, Layout
import pandas as pd
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go

_ = MessageFactory('medialog.plotly')
 

def login(self):
    username = self.portal_registry['medialog.plotly.interfaces.IPlotlySettings.plotly_username']
    api_key  = self.portal_registry['medialog.plotly.interfaces.IPlotlySettings.plotly_api_key']
    plotly.tools.set_credentials_file(username=username, api_key=api_key)
    
def make_basic_graph(self, context):
    """ generating the html from plotly every time URL is changed"""
    
    csv_url = self.csv_url
    title = self.Title()
    name = self.Description() or ''
    
    self.login()
    
    df = pd.read_csv(csv_url)
    df.head()
    axis = df.columns.tolist()
    xaxis = axis[0]
    yaxis = axis[1]
    
    trace = go.Scatter(
              #x-aksis og y-aksis
              x = df[xaxis], y = df[yaxis],
              name=name,
              )
    layout = go.Layout(
              title=title,
              plot_bgcolor='rgb(230, 230,230)',
              showlegend=True
              )
    fig = go.Figure(data=[trace], layout=layout)
    self.plotly_html = plotly.offline.plot(fig, show_link=False, include_plotlyjs = False, output_type='div')
  

def make_bar(self, context):
    """let plottly make bar"""
    
    self.login()

    graph_data = self.graph_data
    chart_type = self.chart_type
    
    y = []
    for item in graph_data:
        y.append(item['value'])
    
    x = []
    for item in graph_data:
        x.append(item['name'])
    
    if chart_type == 'bar':
        data = [go.Bar(
            y=y,
            x=x,
            orientation = 'v'
        )]
        

    if chart_type == 'pie':
        data = [go.Pie(
            labels=x,
            values=y)
        ]

    self.plotly_html = plotly.offline.plot(data, include_plotlyjs = False, show_link=False, output_type='div')