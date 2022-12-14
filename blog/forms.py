from django import forms
from .models import Comment

class NewCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text',]
        help_text = {'text': 'Create a new comment'}