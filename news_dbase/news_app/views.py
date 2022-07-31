# Импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД

from django.views.generic import ListView, DetailView

from .models import Post


class PostsList(ListView):
    model = Post
    ordering = '-post_creation'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 2  # вот так мы можем указать количество записей на странице

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
