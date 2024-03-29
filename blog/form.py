from django import forms
from .models import Comment

#email send form
class EmailPostForm(forms.Form):
        name = forms.CharField(max_length  = 25)
        email = forms.EmailField()
        to = forms.EmailField()
        comment = forms.CharField(required = False ,
                                  widget = forms.Textarea)

#comment form

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email','body')
