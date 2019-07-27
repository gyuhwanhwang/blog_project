from django.shortcuts import render, redirect
from django.contrib.auth.models import User # User에 대한 class를 가져와 준다
from django.contrib import auth # 권한에 대한 내용을 가져와 준다.

def signup(request):
    if request.method == 'POST':    # 회원가입 작성하고 전송버튼 눌렀다면 ( POST 방식 )
        if request.POST.get('password1') == request.POST.get('password2'):
            user = User.objects.create_user( username=request.POST.get('username'), password=request.POST['password1'])
            # User.objects.create_user(username=, password= ) 함수 사용하여 계정 생성
            auth.login(request, user) # 회원가입하면 자동으로 로그인을 하는 함수
            return redirect('home')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=password) # 데이터베이스에서 회원일치하는지 확인
        if user is not None:    # 회원이 아니면 None
            auth.login(request, user)   # 회원이면 로그인
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request,'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)    # auth의 함수 
        return redirect('home')
    return render(request, 'login.html')
