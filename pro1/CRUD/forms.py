from django import forms
from .models import Shopping


class ShoppingForm(forms.ModelForm):
    class Meta:
        model = Shopping
        fields = "__all__"
