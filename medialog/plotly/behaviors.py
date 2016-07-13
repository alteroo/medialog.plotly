from zope import schema
from plone.directives import form
import plone.directives
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides
from zope.i18nmessageid import MessageFactory
from medialog.tablebehavior.widgets.widget import TableFieldWidget

_ = MessageFactory('medialog.plotly')


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
        label=_(u'Graph'),
        fields=[
               'chart_title',
              'chart_type',
              'chart_description',
              'table',
        ],
     )
     
     
    form.widget(table=TableFieldWidget)
    table = schema.Text(
        title=u'Table',
        default=u'[["Year", "A, "B"], [1990, 10, 20]]',
        required=True,
    )  
    
    chart_title = schema.TextLine(
        title=u'Chart Title',
    )

    chart_description = schema.TextLine(
        title=u'Chart Description (y-axis)',
    )
    
  
    chart_type = schema.Choice(
        title=u'Chart type',
        values=[u"table", u"pie", u"bar", u"line", u"map"],
    )


alsoProvides(IPieBehavior, IFormFieldProvider)



class IPlotlyCSVBehavior(form.Schema):
    """ Add graphs from CSV URLs"""
    
    form.fieldset(
        'plotly',
        label=_(u'Plotly'),
        fields=[
              'csv_url',
        ],
     )
         
    csv_url = schema.URI(
        title = _("label_csv_url", default=u"URL to CSV data"),
        description = _("help_csv url",
                      default=""),
        required = False,
     )
    
alsoProvides(IPlotlyCSVBehavior, IFormFieldProvider)


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






