from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import FormView, CreateView
from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import get_object_or_404
from django.core import serializers

from page.models import Pages
from page.forms import PageForumForm

import json

# Create your views here.
class MysitePageLayoutView(ListView):

    template_name = 'page/layout.html'

    def get_queryset(self):
        return Pages.objects.filter(is_active=True)

class MysitePageFormView(FormView):
    template_name = 'page/forum.html'
    form_class = PageForumForm
    success_url = '/page/'

    def form_valid(self, form):
        form.save()
        return super(MysitePageFormView, self).form_valid(form)

class MysitePageCreateView(CreateView):
    model = Pages
    template_name = 'page/forum.html'
    form_class = PageForumForm

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

class MysitePageDetailView(TemplateView):
    def get(self, request, *args, **kwargs):
            my_object = Pages.objects.filter(pk=request.GET['id'])
            json = serializers.serialize("json", my_object)
            return HttpResponse(json, content_type="application/json")        