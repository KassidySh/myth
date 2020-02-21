from django import forms
from .models import Story, Comment

class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ('author','title','god','content')
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author','story','comment')