from django import forms

from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'picture_URL')
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)