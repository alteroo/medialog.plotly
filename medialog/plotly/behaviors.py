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
              'orientation',
              'chart_description',
              'table',
        ],
     )
     
     
    form.widget(table=TableFieldWidget)
    table = schema.Text(
        title=u'Table',
        default=u'[["A", "B"], [1, 10]]',
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
        values=[u"pie", u"bar", u"line", u"map"],
    )

    orientation = schema.Choice(
        title=u'Vertical or Horizontal (if available)',
        values=[u"h", u"v"],
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






