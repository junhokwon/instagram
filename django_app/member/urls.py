from django.conf.urls import url

from member import views

urlpatterns = [
    url(r'^login/$', views.login_fbv, name='login'),
    url(r'^login/$', views.logout, name='logout'),
]