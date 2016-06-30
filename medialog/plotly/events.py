
    
from plone import api
from zope.i18nmessageid import MessageFactory

import urllib

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
    


def make_html(self, context):
    """let plottly make bar"""
    
    title = self.Title()
    name = self.Description() or ''
    self.login()

    chart_type = self.chart_type
 
    if chart_type == 'pie':
        make_pie(self, context, title, name)
        
    if chart_type == 'json':
        make_json_graph(self, context, title, name)
        
def make_pie(self, context, title, name):
    y = []
    x = []
    graph_data = []
    import pdb; pdb.set_trace()
    
    df = pd.read_json(self.table)
    indexes = df.columns.values.tolist()
    
    for index in indexes:
        graph_data.append(df[index].values.tolist())
    
    #there must be a better way to do this
    for items in graph_data:
        x.append(items[0])
        for item in items[1:]:
        	y.append(str(item))
       
    data = [go.Pie(
            labels=x,
            values=y) ]
    
    layout = {'title': title, 'show_link': False}
        
    self.plotly_html = plotly.offline.plot(data, layout, include_plotlyjs = False, output_type='div')
        


def make_json_graph(self, context, title, name):
    """ generating the html from plotly every time URL is changed"""
    
    json_url = self.json_url
    
    df = pd.read_json(json_url)
    
    #maybe do something, if not, we could just skip 'read_json'
    #df.head()
    
    data = df.values.tolist()
    self.plotly_html = plotly.offline.plot(data, include_plotlyjs = False, output_type='div')

 
def make_xhtml(self, context):
    """let plottly make bar"""
    
    title = self.Title()
    name = self.Description() or ''
    self.login()

    graph_data = self.graph_data
    chart_type = self.chart_type
 
    y = []
    y1 = []
    y2 = []
    for item in graph_data:
        y.append(item['values'][0])
        y1.append(item['values'][1])
        y1.append(item['values'][2])
    
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
        
    if chart_type == 'histogram':
        data = [go.Histogram(
            x=x,
            y=y)
        ]
        
    if chart_type == 'line':
        data = go.Line(
              #x-aksis og y-aksis
              )
        layout = go.Layout(
              title=title,
              plot_bgcolor='rgb(230, 230,230)',
              showlegend=True
              )

    self.plotly_html = plotly.offline.plot(data, include_plotlyjs = False, show_link=False, output_type='div')
    

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