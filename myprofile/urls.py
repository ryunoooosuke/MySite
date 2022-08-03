from django.urls import path

from . import views

app_name = 'myprofile'
urlpatterns = [
    path('', views.Index, name='index'),
    path('workdetail/<int:work_id>/', views.WorkDetail, name='work_detail'),
]
