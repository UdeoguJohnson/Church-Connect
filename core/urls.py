from django.contrib import admin
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('dashboard/', views.dashboardView, name= 'dashboard'),
    path('event/', views.createEventView, name= 'event'),
    path('prayer-request/', views.createEventView, name= 'prayer_request'),
    path('memberlist', views.memberListView, name = 'member_list')
]