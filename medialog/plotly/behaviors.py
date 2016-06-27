from zope import schema
from plone.directives import form
import plone.directives
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides
from zope.i18nmessageid import MessageFactory
from collective.z3cform.datagridfield import DataGridFieldFactory 
from collective.z3cform.datagridfield import DictRow

_ = MessageFactory('medialog.plotly')


 
class IPair(form.Schema):
    name = schema.TextLine(
        title=_(u"Name"),
        description=u"",
        required=False,
    )
  
    value = schema.Float(
        title=_(u"Value(s)"),
        description=u"",
        required=False,    
    )       


class IPlotlyBehavior(form.Schema):
    """ Can be 'plotlified' """

    form.mode(plotly_html='hidden')
    plotly_html = schema.Text(
        title=u'Plotly html',
        default=u'',
        required=False,
    )
alsoProvides(IPlotlyBehavior, IFormFieldProvider)
    

class IPieBehavior(form.Schema):
    """Plotly fields"""
    
    form.fieldset(
        'plotly',
        label=_(u'Plotly'),
        fields=[
              'table',
              'graph_data',
              'chart_type',
        ],
     )
    
    table = schema.Text(
        title=u'Table',
        default=u'',
        required=False,
    )  
    
    form.widget(graph_data=DataGridFieldFactory)
    graph_data = schema.List(
         title=_(u"graph_data", 
            default=u"Graph data"),
        description=_(u"help_graph_data",
            default="""Graph Data"""),
        value_type=DictRow(schema=IPair),
        required=False,
    )
    
    form.mode(chart_type='hidden')
    chart_type = schema.TextLine(
        title=u'Chart type',
        default=u"pie",
    )

alsoProvides(IPieBehavior, IFormFieldProvider)


class IPlotlyJsonBehavior(form.Schema):
    """ Add graphs from JSON URLs"""
    
    form.fieldset(
        'plotly',
        label=_(u'Plotly'),
        fields=[
              'json_url',
              'chart_type',
        ],
     )
         
    json_url = schema.URI(
        title = _("label_json_url", default=u"URL to JSON data"),
        description = _("help_json url",
                      default=""),
        required = True,
     )
    
    
    form.mode(chart_type='hidden')
    chart_type = schema.TextLine(
        title=u'Chart type',
        default=u"json",
    )
    
alsoProvides(IPlotlyJsonBehavior, IFormFieldProvider)




class IXPlotlyBehavior(form.Schema):
    """ A field where you can set URL to a CSV file"""
    
    form.fieldset(
        'plotly',
        label=_(u'Plotly'),
        fields=[
              'csv_url',


        ],
     )
     
    csv_url = schema.URI(
        title = _("label_plotly_csv", default=u"CSV URL"),
        description = _("help_plotly_csv",
                      default=""),
        required = False,
     )
    
    
    form.mode(plotly_html='hidden')
    plotly_html = schema.Text(
        title=u'Plotly html',
        default=u'',
        required=False,
    )

alsoProvides(IXPlotlyBehavior, IFormFieldProvider)






