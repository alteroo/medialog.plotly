from zope import schema
from plone.directives import form
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides
from zope.i18nmessageid import MessageFactory

from plone import api

_ = MessageFactory('medialog.plotly')
 
class IPlotlyBehavior(form.Schema):
    """ A field where you can set URL to a CSV file"""
    
    form.fieldset(
        'plotly',
        label=_(u'Plotly'),
        fields=[
              'csv_url',
        ],
     )
     
    csv_url = schema.URI(
        title = _("label_plotly", default=u"CSV URL"),
        description = _("help_plotly",
                      default="CSV URL"),
     )

alsoProvides(IPlotlyBehavior, IFormFieldProvider)

