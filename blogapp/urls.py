from django.contrib import admin
from django.urls import path
# import blogapp.views
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blogapp'
urlpatterns = [
    path('<int:blog_id>', views.detail, name="detail"), # 앞에 /blog/ 지운다, blogapp.views 도 그냥 views. 로 바꾼다
    path('new/', views.new, name="new"),
    path('create', views.create, name="create"),
    path('newblog/', views.blogpost, name="newblog"),   # form에 기반한 함수 실행시켜줄 url
]