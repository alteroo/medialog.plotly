
    
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
    """let plottly make the graph"""
    
    title = self.chart_title
    chart_type = self.chart_type
    ylabel = self.chart_description
    self.login()
    
    df = pd.read_json(self.table)
    
    columnlist = df.columns.tolist()[1:]
    columns = df.values.tolist()
    xaxis = df.take([0], axis=1)

    if chart_type == 'json':
        make_json_graph(self, context, title)
    
    if chart_type == 'pie':
        make_pie(self,  context, title, df, ylabel, columns, columnlist)
    
    if chart_type == 'line':
        make_line(self, context, title, df, ylabel, columnlist)
        
    if chart_type == 'bar':
        make_bar(self, context, title,  df, ylabel, columnlist)
    
    if chart_type == 'map':
        make_map(self, context, title, df, ylabel, columnlist)
    
        
def plot(self, fig):
    self.plotly_html = plotly.offline.plot(fig, show_link=False, include_plotlyjs = False, output_type='div')
        
def make_pie(self, context, title, df, ylabel, columns, columnlist):
    labelline = df.take([0], axis=0)
    #labels are same for all pies
    labels = labelline.values.tolist()[0][1:]
    
    #count number of pies to draw
    graphs = float(len(columns) - 1)
    
    #space needed for each pie
    graphwidth = 1/graphs 
    
    trace = []
    
    for count in df.index[1:]:
        #should be 1, 2, 3 etc.
        valueline = df.take([count], axis=0)
        values = valueline.values.tolist()

        graphsecond = graphwidth * count
        graphfirst = graphsecond -  graphwidth
        trace.append(go.Pie(
              labels = labels, 
              values = values[0][1:],
              name= values[0][0],
              text= values[0][0],
              hole = 0,
              domain = dict(x = [graphfirst, graphsecond]
              ),
             ))

    layout = go.Layout(
              title=title,
              showlegend=True,
    )
    
    
    fig = go.Figure(data=trace, layout=layout)
    plot(self, fig)

def make_line(self, context, title, df, ylabel, columnlist):
    xaxis = df.take([0], axis=1)
    
    trace = []
    
    for count in columnlist:
        y = df[count].tolist()
        x = xaxis.values.tolist()
        
        trace.append(go.Scatter(
              #x-aksis og y-aksis
              x = x, 
              y = y,
              name=y[0],
             ))

    layout = go.Layout(
              title=title,
              showlegend=True,
              xaxis=dict(
                    title=df[0][0],
             ),
                yaxis=dict(
                title=ylabel,
             )
    )
    
    fig = go.Figure(data=trace, layout=layout)
    plot(self, fig)


def make_bar(self, context, title, df, ylabel, columnlist):
    xaxis = df.take([0], axis=1)
    
    trace = []
    
    for count in columnlist:
        y = df[count].tolist()
        x = xaxis.values.tolist()
        
        trace.append(go.Bar(
              #x-aksis og y-aksis
              x = x, 
              y = y,
              name=y[0],
             ))


    layout = go.Layout(
              title=title,
              showlegend=True,
              )
    
    fig = go.Figure(data=trace, layout=layout)
    plot(self, fig)

        
    

def make_map(self, context, title, df, ylabel, columnlist):  
    """ Take data from the graph and make a world map
    Sorted on first column, country codes NOR / USA or names"""
    #Not pretty, but works
    #country should be in first row
    #should look up the index name instead
    locations = df[0][1:]
    #main values should be in second
    z = df[1][1:].values
        
    worlddata = df[1:].values.tolist()
    headings =  df.take([0], axis=0)
    text = []
    
    for country in worlddata:
        textline = ''
        for idx,item in enumerate(country[1:]):
             textlabel = headings[idx+1]
             valeur = item
             textline = textline + textlabel + ': ' +  valeur + '<br>'
        text.append(textline)

    trace = go.Choropleth(
            type = 'choropleth',
            locations = locations,
            z = z,
            text = text,
            marker = dict(
                line = dict (
                    color = 'rgb(180,180,180)',
                    width = 0.5
                ) ),
          )

    layout = go.Layout(
        title = title,
        autosize=True,
        width=1200,
        height=900,
        geo = dict(
            showland = True,
            landcolor = '#f4f5ed',
            subunitwidth = 1,
            countrywidth = 1,
            showframe = False,
            showcoastlines = True,
            projection = dict(
                type = 'Equirectangular'
            )
        )
    )
    
    fig = go.Figure( data=[trace], layout=layout )
    plot(self, fig)
 
def make_json_graph(self, context, title):
    """ generating the html from plotly"""
    false = False
    true = True
    json_url = self.json_url
    
    self.plotly_html = plotly.offline.plot(self, fig)
    
    

