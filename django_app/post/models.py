from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
# 장고가 기본적으로 제공하는 User와 연결


class Post(models.Model):
    title = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    photo = models.ImageField(upload_to='post',blank=True)
    # upload_to = 'post'는 post/~로 이미지파일경로가 정해진다.
    # ImageField는 ImageFileField로 변환된다. 즉 file로 처리한다는것
    # image를 처리하기 위해서 pillow을 깔아야한다.
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name ='like_posts',
        through = 'PostLike',
    )
    tags = models.ManyToManyField('Tag',blank=True)

    def add_comment(self,user,content):
        self.comment_set.create(author=user,content=content)

    def add_tag(self,tag_name):
        tag,tag_created = Tag.objects.get_or_create(name=tag_name)
        if not self.tags.filter(id=tag.id).exists():
            self.tags.add(tag)
            # tags는 다대다관계로 Post와 연결되어있기에, Tag클래스에서 만들어진
            # 속성 name을 가져온.

    @property
    def like_count(self):
        #자신의 Post를 like하고 있는 user수 리턴
        return self.like_users.count()



    def __str__(self):
        return self.title

class PostLike(models.Model):
    post = models.ForeignKey(Post)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name = 'like_comments',
        through = 'CommentLike',
    )

class CommentLike(models.Model):
    comment = models.ForeignKey(Comment)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_date = models.DateTimeField(auto_now_add=True)



class Tag(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return "tag ({})".format(self.name)