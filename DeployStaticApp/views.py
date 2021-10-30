from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.
class MyTemplateView(TemplateView):
    template_name="DeployStaticApp/index.html"
