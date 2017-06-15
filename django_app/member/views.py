from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def login_fbv(request):
    # member/login.html 생성
    # username,password,button이 있는 html 생성
    # post요청이 올경우 좌측 코드를 기반으로 로그인 완료후 post_list로 이동
    # 실패할경우 httpresponse로 login invalid 띄워주기


    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # username,password변수에 할당(문자열)
        # authenticate함수를 사용해서 user객체를 얻어 user에 할당
        # 인증에 실패할 경우는 user변수에는 None이 할당됨
        user = authenticate(
            username=username,
            password=password,
        )
        # user변수가 None이 아닐경우(정상적으로 인증되어 User객체를 얻은경우
        if user is not None:
            login_fbv(request, user)
            # django의 session을 이용해 이번 request,user객체를 사용해 로그인 처리
            return redirect('post:post_list')
        else:
            # 로그인이 실패함
            return HttpResponse('login credentials invalid')


    else:
        #get요청이 왔을경우(다시 login.html로 그려준다.)
        if request.user.is_authenticated:
            return redirect('post:post_list')

        #만약 이미 로그인 된 상태일 경우에는
        # post_list로 redirect
        #아닐경우 login.html을 render에서 다시 리턴
        # 로그인이 되지 않을경우 user는 anonymous user을 가져온다.
        return render(request,"member/login.html",)

def logout(request):
    # 로그아웃되면, post_list로 redirect
    logout(request)
    return redirect('post:post_list')

