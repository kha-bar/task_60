# from django.db import models
from django.urls import reverse

from news_db.models import *


class Post(Post):

    # name = super(Post, self.post_title)

    def __str__(self):
        return f'{self.post_title.title()}: {self.post_text[:20]}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

class Category(Category):

    def __str__(self):
        return self.name_category.title()
