from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import fields
from .models import Profile,Comment,Post
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,Layout,Field


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class PostForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('post', 'post',css_class = 'btn btn-warning m-2' ))

    class Meta:
        model = Post
        fields = [
            'image',
            'caption'
        ]


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment_body',]
        widgets = {
            'comment_body':forms.Textarea(attrs={'class': 'form-control'}),
        }
            