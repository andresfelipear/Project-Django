from django.forms import ModelForm, fields
from .models import Breakfast, Todo

class BreakfastForm(ModelForm):
    class Meta:
        model = Breakfast
        fields = ['name','price']