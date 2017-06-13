from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from post.models import Post, Comment

from django.shortcuts import render
from .models import Post


def post_list(request):
    # 모든 Post목록을 'posts'라는 key로 context에 담아 return render처리
    # post/post_list.html을 template으로 사용하도록 한다

    # 각 포스트에 대해 최대 4개까지의 댓글을 보여주도록 템플릿에 설정
    posts = Post.objects.all()
    context = {
        'posts' : posts,
    }
    return render(request, 'post/post_list.html', context)


def post_detail(request, post_pk):

    # 가져오는 과정에서 예외처리를 한다
    try:
        post = Post.objects.get(pk=post_pk)
    except Post.DoesNotExist as e:
        return HttpResponse('post not found, detail : {}'.format(e))
        # 1. 404 에러를 띄어준다.
        # 2. redirect 함수를 이용하여 post_list로 되돌려준다. redirect는 모델,url의 view_name,절대경로 url
        # redirect(url_name,
        return redirect('post:post_list')

    # 모델(DB)에서 post_pk에 해당하는 Post객체를(인스턴스를 가져와 변수에 할당
    # 한개의 객체를 가져오기 모델매니저(objects)의 get()메서드를 가져온다.
    # request에 대해 response를 돌려줄때는 HttpResponse 나 render를 사용가능
    # template를 사용하려면 render함수를 사용한다.
    # render함수는 django.template.loader.get_template함수와
    # django.http.HttpResponse함수를 축약해놓은 shortcut
    # render함수는 django가 템플릿을 검색 할 수 있는 모든 디렉토리 순회,
    # 인자로 주어진 문자열값과 일치하는 템플릿이 있는지 확인 후,
    # 결과를 리턴 (django.template.backends.django.Template클라스형 객체
    template = loader.get_template('post/post_detail.html')
    # dict형 변수 context의 'post'키에 post객체를 할당
    # context로 전달된 dict의 "키"값이 템플릿에서 사용가능한 변수명이됨
    context = {
        'post' : post,
    }
    # template에 인자로 주어진  context,request,render함수를 사용해서 해당
    #  template를 string으로 전환
    rendered_string = template.render(context=context,request=request)
    # 변환된 string을 HttpResponse형태로 돌려준다.
    return HttpResponse(rendered_string)
    #return render(request, 'post/post_detail.html',context)


# def post_create(request):
#     if request.method == 'GET':
#         context = {
#
#         }
#         return render(request,'post/post_create.html',context)
#
#     elif request.method == 'POST':
#         data = request.POST
#         title = data['title']
#         image = request.FILES['photo']
#         # 파일데이터를 받을때 ,imagefield는 imagefilefield로 변해있기에
#         user = User.objects.first()
#         post = Post.objects.create(
#             title=title,
#             author=user,
#             image=image,
#
#         )
#         return redirect('post:post_detail' , pk=post.pk)
#
#
# def post_modify(request, post_pk):
#     post = Post.objects.get(pk=post_pk)
#     if request.method == 'POST':
#         data = request.POST
#         image = request.FILES['photo']
#         title = data['title']
#         post.title = title
#         post.image = image
#         post.save()
#         return redirect('post:post_detail',pk=post.pk)
#     elif request.method == 'GET':
#         context = {
#             'post' : post,
#         }
#         return render(request,'post/post_modify.html',context)
#
#
# def post_delete(request, post_pk):
#     if request.method == 'POST':
#         post = Post.objects.get(pk=post_pk)
#         post.delete()
#         return redirect('post:post_list')
#     else:
#         return HttpResponse('GET Method은 올 수 없습니다.')
#
#
#
# def comment_create(request, post_pk):
#     if request.method == 'GET':
#         context = {
#
#         }
#         return render(request, 'post/comment_create',context)
#     elif request.method == 'POST':
#         data = request.POST
#         content = data['content']
#         user = User.objects.first()
#         post = Post.objects.all()
#         comments = post.comment_set.create(
#             content = content,
#             author = user,
#
#         )
#         return redirect('post:post_detail',pk=post_pk)
#     # POST요청을 받아 Comment객체를 생성 후 post_detail페이지로 redirect
#
#
# def comment_modify(request, post_pk):
#     comment = Comment.objects.get(pk=post_pk)
#     if request.method == 'POST':
#         data = request.POST
#         content = data['content']
#         comment.content = content,
#         comment.save()
#         return redirect('post:post_detail',pk=post_pk)
#     elif request.method == 'GET':
#         context = {
#             'comment' : comment,
#         }
#         return render(request,'post/comment_modify',context)
#
#
#
# def comment_delete(request, post_pk, comment_pk):
#     # POST요청을 받아 Comment객체를 delete, 이후 post_detail페이지로 redirect
#     if request.method == "POST":
#         post = Post.objects.get(pk=post_pk)
#         comments = post.comment_set.get(pk=comment_pk)
#         comments.delete()
#     else:
#         return HttpResponse('get method은 올수 없습니다.')