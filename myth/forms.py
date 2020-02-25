from django import forms
from .models import Story, Comment, FaveGod, FaveStory

class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ('author','title','god','content')
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author','story','comment')

class FaveGodForm(forms.ModelForm):
    class Meta:
        model = FaveGod
        exclude = ('user','god')
        # fields = ('user', 'god')        

class FaveStoryForm(forms.ModelForm):
    class Meta:
        model = FaveStory
        # fields = ('user', 'story')  
        exclude = ('user','story')