from django.contrib import admin
from django.urls import path
from process import views

urlpatterns = [
    path('',views.showIndex,name='main_page'),
]
