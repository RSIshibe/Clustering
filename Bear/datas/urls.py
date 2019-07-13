from django.conf.urls import url

from . import views

app_name = "datas"
urlpatterns = [
    url(r'^$', views.view_alpha, name='home'),
    url(r'^upload/spreadsheet/$', views.upload_spreadsheet_file, name='upload_spreadsheet'),
]