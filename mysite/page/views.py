from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView

from page.models import Pages
from page.forms import PageCreateForm

# Create your views here.
class MysitePageListView(ListView):

    template_name = 'page/pages_detail.html'

    def get_queryset(self):
        return Pages.objects.filter(is_active=True)

class MysitePageFormView(FormView):
    template_name = 'page/pages_create.html'
    form_class = PageCreateForm

    def form_valid(self, form):
        form.save()
        return super(MysitePageFormView, self).form_valid(form)