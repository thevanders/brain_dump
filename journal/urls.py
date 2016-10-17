from django.conf.urls import url
from . import views

app_name = 'journal'

urlpatterns = [
    url(r'^$', views.IndexView, name='index_view'),
    url(r'^entry/', views.EntryView, name="entry_view"),
]
