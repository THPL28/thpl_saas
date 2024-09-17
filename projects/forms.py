# forms.py

from django import forms



class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu nome'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Seu email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Sua mensagem', 'rows': 5}))
