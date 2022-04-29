from django.forms import ModelForm
from .models import Breakfast

class BreakfastForm(ModelForm):
    class Meta:
        model = Breakfast
        fields = ['name','price','image']