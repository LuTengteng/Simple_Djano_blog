# urls.py
from django.conf.urls import *
from django.views.generic import TemplateView
from blog import views

urlpatterns = [
    url(r'^$', views.archive, name='archive'),
    #url(r'^$', TemplateView.as_view(template_name='archive.html'), name='archive'),
    #url(r'^create',TemplateView.as_view(template_name='archive.html'), name='create_blogpost'),
    url(r'^create',views.create_blogpost, name='create_blogpost'),
    #url(r'^create/', 'create_blogpost'),
]
