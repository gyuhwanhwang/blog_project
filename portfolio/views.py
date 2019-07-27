from django.shortcuts import render, redirect # redirect는 import해줘야됨
from .models import Portfolio # import 해줘야됨
from django.core.paginator import Paginator 

def portfolio(request):
    portfolios = Portfolio.objects
    return render(request, 'portfolio.html',{'portfolios':portfolios})

def new(request): # new.html 띄워주는 함수
    return render(request, 'new_pf.html')
    
def create(request): # 입력받은 내용을 데이터베이스에 넣어주는 함수
    portfolio = Portfolio() # blog라는 변수를 Blog 타입의 객체로 생성해줌
    portfolio.title = request.POST.get('title_pf') # new.html에서 title로 적었던 부분을 변수의 title안에 넣어줌
    portfolio.description = request.POST.get('description')
    portfolio.image = request.FILES.get('image') # 작성된 시간 넣어줌, 위에 import 확인해라!
    portfolio.save() # 쿼리셋 메소드 중에 하나, 이 객체를 데이터베이스에 저장해라
    # 객체.delete() 도 있다. db에서 지움
    return redirect('/portfolio/') # import해야됨, 함수 내용 다 처리하고 URL로 이동해라
    # str을 써준 이유 --> url은 항상 str인데 portfolio.id는 int형이기 때문에 문자열로 형변환을 시켜준거

    # class Portfolio(models.Model):
    #     title = models.CharField(max_length = 255)
    # image = models.ImageField(upload_to = 'images/') # media 경로 디렉토리 바로 아래에 위치
    # description = models.CharField(max_length = 500)