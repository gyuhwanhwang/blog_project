from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='portfolio'
urlpatterns = [
    path('', views.portfolio, name="portfolio"),
    path('new/', views.new, name="new"),
    path('create', views.create, name="create"),
]