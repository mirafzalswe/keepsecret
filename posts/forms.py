from django import forms
from .models import Post, Comment, Hashtag

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'hashtags']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class HashtagsForm(forms.ModelForm):
    class Meta:
        model = Hashtag
        fields = ['name']