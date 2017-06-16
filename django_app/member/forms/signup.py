from django.contrib.auth import authenticate, get_user_model

from django.http import HttpResponse
from django import forms
#장고에있는 form을 가져와야한다.

User =get_user_model()




class SignupForm(forms.Form):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        # ':' 추가

    username = forms.CharField(
        label='유저이름',
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'placeholder': '사용자 아이디를 입력하세요',
            }
        )
    )
    nickname = forms.CharField(
        max_length=24,
        widget=forms.TextInput(
            attrs={
                'placeholder' : '닉네임을 입력하세요',
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'password1를 입력하세요',
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder' : 'password2를 입력하세요',
            }
        )
    )

    # is_valid를 실행했을 때, Form내부의 모든 field들에 대한
    # 유효성 검증을 실행하는 메서드
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                'Username already exist'
            )
        return username

    def clean_nickname(self):
        nickname = self.cleaned_data['nickname']
        if User.objects.filter(nickname=nickname).exists():
            raise forms.ValidationError(
                'nickname already exist'
            )
        return nickname

    def clean_password2(self):

        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        #get메서드를 사용해도
        if password1 and password2 and password1 !=password2:
            raise forms.ValidationError(
                'PASSWORD NOT EQUAL'
            )
        return password1

    def create_user(self):
        username = self.cleaned_data['username']
        password1 = self.cleaned_data['password1']

        user = User.objects.create_user(
            username=username,
            password=password1,
        )
        return user
