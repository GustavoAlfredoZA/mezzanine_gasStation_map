from django.conf.urls import url, include
#from django.urls import path
from django.conf.urls import url
from . import views
from mezzanine_map.views import map_View,map

urlpatterns = [
#    url('',views.index,name='index'),
    url(r'^map', map_View.as_view()),
]
