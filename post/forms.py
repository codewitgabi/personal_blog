from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
	content = forms.CharField(widget=forms.Textarea(
		attrs={
			"placeholder": "Enter Comment",
			"rows": "4",
		}
	))
	class Meta:
		model = Comment
		fields = ["content"]