"""instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.contrib import admin
from post import views as post_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^post/', include('post.urls')),
    # config에 항상 포함되는 공통적인 url요소를 넣어준다. 그리고
    # include(post.urls) : post.urls의 모든 정규표현식을 포함해라
    # include를 import했기 때문에 경로지정이 필요없다.
]

urlpatterns += static(
        prefix = settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
)

# urls.py에 media 파일을 제공하는 url패턴등록부분을 고친다.
# static 함수에 첫번째 인자로 media file url,키워드인자 document_root로 media file이 위치한 경로
