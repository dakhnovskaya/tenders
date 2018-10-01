from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.tender_list, name='tender_list'),
]