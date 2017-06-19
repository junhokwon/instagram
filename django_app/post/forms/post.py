from django import forms

from ..models import Post


class PostForm(forms.ModelForm):
    # 생성자를 조작해서 실제 Post의 photo필드는 blank=True
    #   (Form에서 required=False)이지만,
    #   Form을 사용할때는 반드시 photo를 받도록 함
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['photo'].required = True

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
        commit = kwargs.get('commit',True)
        # 전달된 키워드인수중 'commit'키 값을 가져옴
        author = kwargs.pop('author',None)
        # 전달된 키워드인수중 'author'키 값을 가져오고,
        # 기존 kwargs dict에서 제외

        self.instance.author = author
        instance = super().save(**kwargs)

        comment_string = self.cleaned_data['comment']
        if commit and comment_string:
            instance.comment_set.create(
                author=instance.author,
                content=comment_string,
            )

        return instance

