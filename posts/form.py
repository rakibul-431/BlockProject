from django import forms
from posts.models import Post,comment

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        exclude=['author']

class CommentForm(forms.ModelForm):
    class Meta:
        model=comment
        fields=['name','body']