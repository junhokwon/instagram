from django import forms

from post.models import Comment


class CommentForm(forms.ModelForm):


    content = forms.CharField(
        required=True,
        widget=forms.TextInput
    )


    class Meta:
        model = Comment
        fields = (
            'content',
        )

    def save(self,**kwargs):
        commit = kwargs.get('commit',True)
        author = kwargs.pop('commit',None)


        self.instance.author = author
        instance = super().save(**kwargs)

        comment_string = self.cleaned_data['comment']
        if commit and comment_string:
            instance.comment_set.create(
                author = instance.author,
                post = instance,
                content = comment_string,
            )
        else:
            instance.comment_set = Comment.objects.create(
                author=author,
                post=instance,
                content=comment_string,
                )
            instance.save()
        return instance

