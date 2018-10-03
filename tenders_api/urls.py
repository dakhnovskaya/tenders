from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.tender_list, name='tender_list'),
    url(r'^tender/(?P<pk>\d+)/$', views.tender_detail, name='tender_detail'),
    url(r'^tender/new/$', views.tender_new, name='tender_new'),
    url(r'^tender/(?P<pk>\d+)/edit/$', views.tender_edit, name='tender_edit'),
]