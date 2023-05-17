from django.forms import ModelForm
from .models import Post


class NewsForm(ModelForm):
    class Meta:
        model = Post
        fields = ['categoryType', 'title', 'authorArticle', 'text']

