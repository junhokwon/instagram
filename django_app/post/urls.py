from django.conf.urls import url

from . import views

app_name = 'post'
urlpatterns = [
    url(r'^$', views.post_list,name='post_list'),
    # views파일의 post_list클래스명
    # 즉 views파일의 post_list클래스로 보내겠다.
    # 정규표현식에서 매칭된 그룹을 위치인수로 반환하는 방법
    # url(r'^(\d+)/$', views.post_detail),

    # 정규표현식에서 키워드인수 (?p<post_pk>\d+)로 주는방법
    url(r'^(?P<post_pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^/create/$', views.post_create, name='post_create'),
    url(r'^(?P<post_pk>\d+)/modify/$', views.post_modify, name='post_modify'),
    url(r'^(?P<post_pk>\d+)/delete/$', views.post_delete, name='post_delete'),
]

app_name = 'comment'
urlpatterns = [
    url(r'^/create/$', views.comment_create,name='comment_create'),
    url(r'^(?P<post_pk>\d+)/delete/$', views.comment_delete,name='comment_delete'),
    url(r'^(?P<post_pk>\d+)/modify/$', views.comment_modify,name='comment_modify'),
]