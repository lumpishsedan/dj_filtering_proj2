import django_filters
from .models import Post

class FilterByKey(django_filters.Filterset):

    class Meta
        model = Post
        fields = ('keyone', 'text')
