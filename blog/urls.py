from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogView, name='blog-views'),
] 