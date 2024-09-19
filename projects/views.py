# projects/views.py

from django.shortcuts import render, redirect
from django.core.cache import cache
import requests
from django.core.mail import send_mail
from .forms import ContactForm
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

# def project_list(request):
#     repos = cache.get('repos')
    
#     if repos is None:
#         username = 'THPL28'
#         url = f'https://api.github.com/users/{username}/repos'
#         try:
#             response = requests.get(url)
#             response.raise_for_status()
#             repos = response.json()
#             cache.set('repos', repos, timeout=60*60)  # Cache por 1 hora
#         except requests.RequestException as e:
#             repos = []
#             print(f"Erro ao buscar repositórios: {e}")
#             messages.error(request, "Erro ao buscar os repositórios do GitHub.")
    
#     return render(request, 'projects/index.html', {'repos': repos})


def project_list(request):
    repos = cache.get('repos')
    languages = []  # Para armazenar as linguagens disponíveis
    
    # Pega a linguagem do filtro na URL (se houver)
    selected_language = request.GET.get('language')

    if repos is None:
        username = 'THPL28'
        url = f'https://api.github.com/users/{username}/repos'
        try:
            response = requests.get(url)
            response.raise_for_status()
            repos = response.json()
            cache.set('repos', repos, timeout=60*60)  # Cache por 1 hora
        except requests.RequestException as e:
            repos = []
            print(f"Erro ao buscar repositórios: {e}")
            messages.error(request, "Erro ao buscar os repositórios do GitHub.")

    # Cria a lista de linguagens únicas dos repositórios
    for repo in repos:
        language = repo.get('language')
        if language and language not in languages:
            languages.append(language)
    
    # Filtra os repositórios pela linguagem selecionada
    if selected_language:
        repos = [repo for repo in repos if repo.get('language') == selected_language]

    return render(request, 'projects/index.html', {
        'repos': repos,
        'languages': languages,
        'selected_language': selected_language
    })

    
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
                subject=f'Nova mensagem de {name}', 
                message=message,    
                from_email=email, 
                recipient_list=['tiago.looze28@gmail.com'],  # Email de destino
                fail_silently=False,  # Para exibir erros se ocorrerem
            )
            messages.success(request, 'Mensagem enviada com sucesso!')
            return redirect('contact')  # Redireciona para a página de contato após o envio
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def under_development(request):
    return render(request, 'under_development.html')