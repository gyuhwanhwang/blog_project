"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # include 는 urls을 앱별로 관리하기 위해서
import blogapp.views
import portfolio.views
### media 파일을 사용하기 위해 import 해줘야 되는것 2가지
from django.conf import settings # configuration, settings에서 media url, root 가져와야함
from django.conf.urls.static import static # configuration에 static이라는 것을 한번 더 import 해줘야됨
### media 파일을 사용하기 위해 import 해줘야 되는것 2가지

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.home, name="home"),
    # path('blog/<int:blog_id>', blogapp.views.detail, name="detail"), blog 다 지워줌
    # path('blog/new/', blogapp.views.new, name="new"),
    # path('blog/create', blogapp.views.create, name="create"),
    path('blog/', include('blogapp.urls', namespace="blogapp")), # blogapp 앱의 urls 파일을 include 해와라, 그리고 그 형식은 blog/로 하겠다.
    # path('portfolio/', portfolio.views.portfolio, name="portfolio"),
    path('portfolio/', include('portfolio.urls', namespace="portfolio")),
    path('accounts/', include('accounts.urls', namespace="accounts")), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # 병렬적으로 media url을 추가해줌

#또는 
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
