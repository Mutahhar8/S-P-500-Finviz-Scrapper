from django.contrib import admin
from django.urls import path
from FinvizApp import views

urlpatterns = [
    path('wikipedia',views.Show_Wikipedia,name='wikipedia'),
    path('details',views.Show_Details,name='details'),
    path('page',views.page,name='page'),
    path('graph',views.Graph_data,name='graph')
]
