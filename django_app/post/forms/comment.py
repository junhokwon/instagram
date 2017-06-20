from django import forms

from post.models import Comment


class CommentForm(forms.ModelForm):

    # comment = forms.CharField(
    #     required=False,
    #     widget=forms.TextInput
    # )
    #

    class Meta:
        model = Comment
        fields = [
            'content',
        ]
        widgets = {
            'content': forms.TextInput(
                attrs={
                    'class': 'input-comment',
                    'placeholder': '댓글달기',
                }
            )
        }
        #필드를 리스트로 구성, 튜플일경우 수정하지 못함

    def clean_content(self):
        content = self.cleaned_data['content']
        if len(content) <3:
            raise ValueError('댓글은 최소 3자이상')
        return content



