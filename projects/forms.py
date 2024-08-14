# forms.py

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'name', 'required': True}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'email', 'required': True}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'message', 'rows': 5, 'required': True}))
