from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

import plotly 
plotly.tools.set_credentials_file(username='medialog', api_key='3tvt5goyi0')

from plotly.graph_objs import Bar, Scatter, Figure, Layout

import pandas as pd
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go


class PlotView(BrowserView):
    """ plot something """
    

    def xmake_plot(self):
        """https://plot.ly/python/getting-started/"""

        context = self.context
        
        data = [go.Bar(
            x=[20, 14, 23],
            y=['giraffes', 'orangutans', 'monkeys'],
            orientation = 'h'
        )]

        mydiv = plotly.offline.plot(data, filename='mygraph', include_plotlyjs = False, output_type='div', auto_open=True)
        
        #context.somefield = mydiv
        return mydiv
        
        
    def make_plot(self):
        """https://plot.ly/python/getting-started/"""

        context = self.context
        title = context.Title()
        name = context.Description() or ''
        
        df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv')

        df.head()
        
        trace = go.Scatter(
                  #x-akse og y-akse
                  x = df['AAPL_x'], y = df['AAPL_y'],
                  name=name,
                  )
        layout = go.Layout(
                  title=title,
                  plot_bgcolor='rgb(230, 230,230)',
                  showlegend=True
                  )
        fig = go.Figure(data=[trace], layout=layout)

        mydiv = plotly.offline.plot(fig, filename='apple-stock-prices', show_link=False, include_plotlyjs = False, output_type='div', auto_open=True)

        return mydiv