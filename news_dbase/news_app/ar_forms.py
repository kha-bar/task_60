from django import forms
from django.core.exceptions import ValidationError
from .models import Post


class PostForm(forms.ModelForm):
   class Meta:
       model = Post
       # fields = '__all__'
       fields = [
           'post_title',
           'post_creation',
           'post_text',
           'post_category',
       #     'price',
       ]
       def clean(self):
           cleaned_data = super().clean()
           description = cleaned_data.get("description")
           if description is not None and len(description) < 20:
               raise ValidationError({
                   "description": "Описание не может быть менее 20 символов."
               })

           name = cleaned_data.get("post_title")
           if name == description:
               raise ValidationError(
                   "Описание не должно быть идентично названию."
               )

           return cleaned_data

#
# class ProductForm(forms.ModelForm):
#     description = forms.CharField(min_length=20)
#
#     class Meta:
#         model = Product
#         fields = [
#             'name',
#             'description',
#             'category',
#             'price',
#             'quantity',
#         ]
#
#     def clean(self):
#         cleaned_data = super().clean()
#         name = cleaned_data.get("name")
#         description = cleaned_data.get("description")
#
#         if name == description:
#             raise ValidationError(
#                 "Описание не должно быть идентично названию."
#             )
#
#         return cleaned_data