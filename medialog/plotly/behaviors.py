from zope import schema
from plone.directives import form
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides
from zope.i18nmessageid import MessageFactory
from zope.interface import Interface
from zope.interface import implements

from plone import api


#plotly stuff
import plotly 
from plotly.graph_objs import Bar, Scatter, Figure, Layout
import pandas as pd
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go






_ = MessageFactory('medialog.plotly')
 
class IPlotlyBehavior(form.Schema):
    """ A field where you can set URL to a CSV file"""
    
    form.fieldset(
        'plotly',
        label=_(u'Plotly'),
        fields=[
              'csv_url',
              'plotly_html',
        ],
     )
     
    csv_url = schema.URI(
        title = _("label_plotly", default=u"CSV URL"),
        description = _("help_plotly",
                      default="CSV URL"),
     )
     
    plotly_html = schema.Text(
        title=u'Plotly html',
        default=u'',
        required=False,
    )

alsoProvides(IPlotlyBehavior, IFormFieldProvider)





class PlotlyBehavior(Interface):
    """ find it"""
    
    
    def plotly(self, context):
        """https://plot.ly/python/getting-started/"""

        csv_url = context.csv_url
        
        #login / api stuff
        username = context.portal_registry['medialog.plotly.interfaces.IPlotlySettings.plotly_username']
        api_key  = context.portal_registry['medialog.plotly.interfaces.IPlotlySettings.plotly_api_key']
        plotly.tools.set_credentials_file(username=username, api_key=api_key)
        
        title = context.Title()
        name = context.Description() or ''
        
        
        df = pd.read_csv(csv_url)
        df.head()
        
        trace = go.Scatter(
                  #x-aksis og y-aksis
                  x = df['AAPL_x'], y = df['AAPL_y'],
                  name=name,
                  )
        layout = go.Layout(
                  title=title,
                  plot_bgcolor='rgb(230, 230,230)',
                  showlegend=True
                  )
        fig = go.Figure(data=[trace], layout=layout)
        context.plotly_html = plotly.offline.plot(fig, show_link=False, include_plotlyjs = False, output_type='div')
        return  plotly.offline.plot(fig, show_link=False, include_plotlyjs = False, output_type='div')
      
    
