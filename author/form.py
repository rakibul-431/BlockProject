from author.models import Author
from django import forms

class AuthorForm(forms.ModelForm):
    class Meta:
        model=Author
        fields=['name','bio','phone_no']