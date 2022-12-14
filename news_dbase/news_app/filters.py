from django_filters import FilterSet, ModelChoiceFilter
from .models import Post

# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class PostFilter(FilterSet):
   class Meta:
       name = ModelChoiceFilter(field_name='post_title',
                                queryset=Post.objects.all(),
                                label='NAME')

       # В Meta классе мы должны указать Django модель,
       # в которой будем фильтровать записи.
       model = Post
       # В fields мы описываем по каким полям модели
       # будет производиться фильтрация.
       fields = {
           # поиск по названию
           'post_title': ['contains'],
           'post_creation': ['date'],
           'post_category': ['contains'],
       }