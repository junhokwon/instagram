from django.db import models
from django.contrib.auth.models import User
# 장고가 기본적으로 제공하는 User와 연결


class Post(models.Model):
    title = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User)
    photo = models.ImageField(blank=True)
    # image를 처리하기 위해서 pillow을 깔아야한다.
    like_users = models.ManyToManyField(
        User,
        related_name ='like_posts',
    )
    tags = models.ManyToManyField('Tag')


    def __str__(self):
        return self.title




class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.ForeignKey(User)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)



class Tag(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return "tag ({})".format(self.name)