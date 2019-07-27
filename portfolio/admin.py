from django.contrib import admin
from .models import Portfolio # 같은 폴더 내 .models.py로부터 Portfolio 클래스를 import

admin.site.register(Portfolio)