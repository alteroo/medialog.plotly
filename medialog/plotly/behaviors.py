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

    value = schema.Int(
        title=_(u"Value"),
        description=u"",
        required=False,
    ) 
    


class IPlotlyBehavior(form.Schema):
    """ A field where you can set URL to a CSV file"""
    
    form.fieldset(
        'plotly',
        label=_(u'Plotly'),
        fields=[
              'csv_url',
              'plotly_html',
              'graph_values',
              'graph_data'
        ],
     )
     
    csv_url = schema.URI(
        title = _("label_plotly_csv", default=u"CSV URL"),
        description = _("help_plotly_csv",
                      default=""),
        required = False,
     )
    
    graph_values = schema.Tuple(
        title = _("label_plotly_graph_values", default=u"Graph Values"),
        description = _("help_plotly",
                      default="CSV URL"),
        required=False,
        default=(),
        missing_value=(),
        value_type=schema.Int(title=u"Int"),
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
    
    form.mode(plotly_html='hidden')
    plotly_html = schema.Text(
        title=u'Plotly html',
        default=u'',
        required=False,
    )

alsoProvides(IPlotlyBehavior, IFormFieldProvider)






