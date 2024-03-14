from django import forms
from category.models import Category,Product


class CategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"