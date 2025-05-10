from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('page/', views.page, name='page'),
    path('case1/', views.case1_page, name='case1_page'),
]