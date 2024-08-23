# projects/views.py

from django.shortcuts import render, redirect
import requests
from django.core.mail import send_mail
from .forms import ContactForm
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

    
def project_list(request):
    username = 'THPL28'
    url = f'https://api.github.com/users/{username}/repos'
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        repos = response.json()
    except requests.RequestException as e:
        repos = []
        print(f"Erro ao buscar repositórios: {e}")

    return render(request, 'projects/index.html', {'repos': repos})

def about(request):
    # Adicione esta view para a página About
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Enviar e-mail
            send_mail(
                f'Contato de {name}',
                message,
                email,
                ['thpldevweb@gmail.com'],
                fail_silently=False,
            )

            return redirect('contact')  # Redireciona após o envio
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def under_development(request):
    return render(request, 'under_development.html')