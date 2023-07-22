from django import forms
from .models import Tag, Post, Categories, Comment


class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple, required=False
    )

    categories = forms.ModelMultipleChoiceField(
        queryset=Categories.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Post
        fields = ("title", "body", "tags", "categories")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment"]
