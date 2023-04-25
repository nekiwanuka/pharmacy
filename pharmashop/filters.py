import django_filters
from .models import Category, Product, Sale
#creating a class to filter models 
class Product_filter(django_filters.FilterSet):
    class Meta: #modify content of other class
        model = Product
        fields = ['item_name']


class Category_filter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = ['name']
        

    
