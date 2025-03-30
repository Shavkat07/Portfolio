from django import forms
from .models import Comment, Messages


class BlogsCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['parent_comment', 'name', 'email', 'text', ]
        labels = {
            'name': 'Name',
            'email': 'Email',
            'text': 'Comment',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name', 'id': 'author'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'id': 'email'}),
            'text': forms.Textarea(attrs={'placeholder': 'Write your message', 'id': 'comment'}),
        }


class SendMessageForm(forms.ModelForm):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Your Name', 'id': "name"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your Email', 'id': "email"}))
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Write your message', 'id': "message", 'cols': "30", 'rows': "10"}))

    class Meta:
        model = Messages
        fields = ['name', 'email', 'message']


