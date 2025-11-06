from django import forms
from .models import Comment

class GuestCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']
        widgets = {'text': forms.Textarea(attrs={'rows':4})}

class AuthCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {'text': forms.Textarea(attrs={'rows':4})}
