from django import forms

from ..models import Post,Comment


class PostForm(forms.ModelForm):
    # 생성자를 조작해서 실제 Post의 photo필드는 blank=True
    #   (Form에서 required=False)이지만,
    #   Form을 사용할때는 반드시 photo를 받도록 함
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['photo'].required = True
        if self.instance.my_comment:
            self.fields['comment'].initial = self.instance.my_comment.content

    comment = forms.CharField(
        required=False,
        widget=forms.TextInput
    )


    class Meta:
        model = Post
        fields = (
            'photo',
            'comment',
        )

    # def save(self,**kwargs):
    #     # save메서드는 키워드인자 한개 `commit=True`만을 받는다.
    #     # post = form.save(commit=False, author=request.user)
    #     # 인자가 2개다. author키를 삭제하고 다시전달한다. 왜냐면 save메서드는 인자 1개만 받는다.
    #
    #     commit = kwargs.get('commit',True)
    #     # 전달된 키워드인자중 'commit'키 값을 가져옴
    #     author = kwargs.pop('author',None)
    #     # 전달된 키워드인자중 'author'키값을 가져오고, 기존 kwargs dict에서 제외
    #
    #
    #     # super()의 save()메서드 호출
    #     instance = super().save(**kwargs)
    #
    #     # ModelForm의 save()메서드를 사용해서 DB에 저장된
    #     # commit(db)에 저장하며,
    #     # (author가 None 또는 author.is_authenticated=False)가 아닌경우
    #     # author가 존재하면서, is_authenticated인경우가 아닌경우,
    #     if commit and not (author and author.is_authenticated):
    #         raise ValueError(
    #             'author is require field'
    #         )
    #
    #     # Post instance(pk를가짐)을 가져옴
    #     # ModelForm에서 commit=True일경우 db에 저장하고(post.objects.create(인자))
    #     # commit=False 일경우 p = Post()와 같기때문에, 인스턴스만 남겨둔다.
    #
    #
    #     # commit은 True로 instance가 pk,author를 정상적으로
    #     # 가진경우에만 Comment생성 로직을 진행
    #     # + comment 필드가 채워져 있을경우,
    #     comment_string = self.cleaned_data['comment']
    #     if commit and comment_string:
    #         instance.comment_set.create(
    #             author=instance.author,
    #             content = self.comment,
    #         )
    #     #modelform의 save()메서드에서 반환해야하는 model의 인스턴스
    #     return instance

    def save(self,**kwargs):
        # self는 여기서 boundform이다. form = PostForm(data=request.POST,files=request.FILES)
        commit = kwargs.get('commit',True)
        # 전달된 키워드인수중 'commit'키 값을 가져옴
        # commit키에 대한 값이 주어지지 않을경우 , commit=True이다.
        author = kwargs.pop('author',None)
        # 전달된 키워드인수중 'author'키 값을 가져오고,
        # 기존 kwargs dict에서 제외한다.
        # 이유는 save()메서드는 한개의 키워드인자밖에 못받는다.



        self.instance.author = author
        # class BaseModelForm(BaseForm):에서 instance가 있건 없건,
        # self.instance = opts = self._meta로 class Meta:에서 만들어 주었던,
        # photo와 comment가 들어있는 인스턴스를 생성해준다.
        # self.instance = instance라고 instance을 self.instance에 할당한다.
        # 즉, 이미 save()메서드를 실행했을때부터, self.instance는 생성되어있음.
        # 요청받은 author=request.user에서 author를 self.instance.author에 할당

        instance = super().save(**kwargs)
        # super()의 save()호출하여 새로 저장


        # commit인수가 True이며, comment필드가 채워져 있을경우 Comment생성 로직을 진행
        # 해당 Comment에서는 instance의 my_comment필드를 채워준다.
        #(이 위에서 super().save()를 실행하기 때문에,
        # 현재위치에서는 author나 pk의 검증이 끝난상태

        comment_string = self.cleaned_data['comment']


        if commit and comment_string:
            #my_comment가 이미 있을경우,(update의 경우)
            if instance.my_comment:
                instance.my_comment.content = comment_string,
                instance.my_comment.save()

            # my_comment가 없을경우,Comment객체를 생성해서, my_comment OTO field에 할
            else:
                instance.my_comment = Comment.objects.create(
                    post=instance,
                    author=author,
                    content=comment_string,
                )
            # OTO필드의 저장을 위해 Post의 save()호출
            instance.save()

            #Model Form의 save()메서드에서 반환해야 하는 model의 인스턴스 리턴
        return instance


