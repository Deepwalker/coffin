from django.views.generic import edit
from coffin.views.decorators import template_response

__all__ = ['CreateView', 'UpdateView', 'DeleteView']

CreateView, UpdateView, DeleteView, FormView = [
        template_response(getattr(edit, view)) for view in (
        'CreateView', 'UpdateView', 'DeleteView', 'FormView'
    )]

