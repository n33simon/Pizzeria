from django import forms
from .models import Comment, Pizza

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text','pizza']
        labels = {'description': 'What would you like to say?'}

