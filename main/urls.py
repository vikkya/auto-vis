from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    url(r'^data/$', views.viewCSV)

]
