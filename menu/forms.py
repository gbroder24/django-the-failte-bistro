from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Form class for users to request a comment
    """
    class Meta:
        model = Comment
        fields = ('content',)
