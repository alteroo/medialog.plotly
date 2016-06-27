"""Table Widget Implementation

$Id$
"""
__docformat__ = "reStructuredText"
import zope.component
import zope.interface
import zope.schema.interfaces

from z3c.form import interfaces
from z3c.form.widget import Widget, FieldWidget
from z3c.form.browser import widget

@zope.interface.implementer_only(interfaces.ITextWidget)
class TableWidget(widget.HTMLTextInputWidget, Widget):
    """Input type text widget implementation."""

    klass = u'table-widget'
    css = u'table'
    value = u''

    def update(self):
        super(TableWidget, self).update()
        widget.addFieldClass(self)


@zope.component.adapter(zope.schema.interfaces.IField, interfaces.IFormLayer)
@zope.interface.implementer(interfaces.IFieldWidget)
def TableFieldWidget(field, request):
    """IFieldWidget factory for TableWidget."""
    return FieldWidget(field, TableWidget(request))