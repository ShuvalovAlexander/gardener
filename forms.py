from django import forms
from .models import Feedback
from .models import Order

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'phone', 'agree']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Имя*'}),
            'phone': forms.TextInput(attrs={'placeholder': '+7 (XXX) XXX-XX-XX'}),
            'agree': forms.CheckboxInput(),
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'price', 'email', 'phone', 'address', 'comment']
        widgets = {
            'product': forms.HiddenInput(),
            'price': forms.HiddenInput(),
            'email' : forms.TextInput(attrs={'placeholder': 'Email*'}),
            'phone' : forms.TextInput(attrs={'placeholder': 'Телефон*'}),
            'address': forms.Textarea(attrs={'rows': 3,'placeholder': 'Адресс доставки*'}),
            'comment': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Коментарий к заказу'}),
        }