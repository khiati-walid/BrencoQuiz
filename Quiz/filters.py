import django_filters
from .models import *

class QuestionFilter(django_filters.FilterSet):
    class Meta:
        model = QuesModel
        fields = ['category']