from django.forms import ModelForm
#accessing our models
from .models import *


class Addform(ModelForm):
    class Meta:
        model = Product
        fields = ['recieved_quantity']


class SaleForm(ModelForm):
    class Meta:
        model = Sale
        fields = ['quantity','amount_received', 'issue_to']
