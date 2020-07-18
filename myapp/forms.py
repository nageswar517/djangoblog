from django import forms
from myapp.models import Comment

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['comment']