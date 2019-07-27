from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone # timezone.datetime.now() 쓰기 위해
from django.core.paginator import Paginator # 페이지네이션을 위해
from .models import Blog
from .form import BlogPost  # form의 BlogPost import 해오기

def home(request):
    blogs = Blog.objects
    
    # 페이지네이션
    # 블로그 모든 글들을 대상으로
    blog_list = Blog.objects.all()
    # 블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(blog_list, 4) # 모든 블로그 객체(blog_list)를 대상으로 3개를 하나의 페이지로
    # request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아내고)
    page = request.GET.get('page') # key값이 page인 value를 얻어냄 (워드 참조)
    # request된 페이지를 얻어온 뒤 return 해 준다
    posts = paginator.get_page(page) # posts라고 하는 변수에는 request된 페이지가 받아짐

    return render(request, 'home.html',{'blogs':blogs, 'posts':posts})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)

    return render(request, 'detail.html', {'blog':blog_detail})

def new(request): # new.html 띄워주는 함수
    return render(request, 'new.html')

def create(request): # 입력받은 내용을 데이터베이스에 넣어주는 함수
    blog = Blog() # blog라는 변수를 Blog 타입의 객체로 생성해줌
    blog.title = request.GET.get('title') # new.html에서 title로 적었던 부분을 변수의 title안에 넣어줌
    blog.body = request.GET.get('body')
    blog.pub_date = timezone.datetime.now() # 작성된 시간 넣어줌, 위에 import 확인해라!
    blog.save() # 쿼리셋 메소드 중에 하나, 이 객체를 데이터베이스에 저장해라
    # 객체.delete() 도 있다. db에서 지움
    return redirect('/blog/'+str(blog.id)) # import해야됨, 함수 내용 다 처리하고 URL로 이동해라
    # str을 써준 이유 --> url은 항상 str인데 blog.id는 int형이기 때문에 문자열로 형변환을 시켜준거
    
def blogpost(request):  # form에 입력
    # 1. 입력된 내용을 처리하는 기능 --> POST

    if request.method == 'POST': 
        form = BlogPost(request.POST)
        if form.is_valid(): # 유효성 검사 올바르면 True
            # form.save() 해도 상관은 없는데 title과 body만 입력받았음, pub_date 넣어줘야됨
            post = form.save(commit=False)  # 모델 객체를 가져오되, 저장하지 않고 가져온다/ post는 blog형 객체
            post.pub_date = timezone.now()
            post.save() # post 저장
            return redirect('home')

    # 2. 빈 페이지를 띄워주는 기능 --> GET
    else:      
        form = BlogPost() # 빈 객체 form이 생성됨
        return render(request, 'new.html', {'form':form}) # 빈 객체 딕셔너리형으로 보내줌