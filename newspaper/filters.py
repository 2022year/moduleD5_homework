from django_filters import FilterSet
from .models import Post

# создаём фильтр
class PostFilter(FilterSet):
    # В мета классе надо предоставить модель и указать поля, по которым будем фильтровать
    class Meta:
        model = Post
        fields = {
            'dateCreated': ['gt'],
            'title':['icontains'],
            'authorArticle': ['exact']
        }
