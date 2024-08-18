# THPL SaaS Portfolio

Este projeto é um portfólio SaaS desenvolvido com Django, mostrando meus projetos, habilidades e informações de contato. O objetivo é criar uma plataforma profissional para compartilhar meu trabalho com o mundo.

## Funcionalidades

- **Página Inicial:** Contém uma apresentação e detalhes sobre mim, junto com links para meus projetos e redes sociais.
- **Projetos:** Uma lista de todos os projetos hospedados no meu GitHub, com descrições detalhadas.
- **Sobre:** Uma página detalhando minhas habilidades, experiência e formação acadêmica.
- **Contato:** Um formulário para entrar em contato comigo por e-mail.

## Tecnologias Utilizadas

- **Django:** Framework web usado para o desenvolvimento do backend.
- **HTML/CSS/Bootstrap:** Usado para a construção das páginas front-end.
- **Python:** Linguagem de programação principal do projeto.
- **GitHub Pages:** Para hospedar a página inicial estática do portfólio.

## Configuração do Projeto

### Requisitos

- **Python 3.x**
- **Django 4.x**
- **Git**

### Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/THPL28/thpl_sas.git
   cd thpl_sas

2.Crie e ative um ambiente virtual:

   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   .\venv\Scripts\activate   # Windows

3.Instale as dependências:
   pip install -r requirements.txt
   
4.Execute as migrações:
   python manage.py migrate

5.Inicie o servidor de desenvolvimento: 
   python manage.py runserver

6.Acesse o site no seu navegador em http://127.0.0.1:8000.


## Configuração de Email
Para habilitar o envio de e-mails pelo formulário de contato, configure as variáveis no arquivo settings.py:

   EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
   EMAIL_HOST = 'smtp.gmail.com'
   EMAIL_PORT = 587
   EMAIL_USE_TLS = True
   EMAIL_HOST_USER = 'seu_email@gmail.com'
   EMAIL_HOST_PASSWORD = 'sua_senha'
   DEFAULT_FROM_EMAIL = 'seu_email@gmail.com'
   

## Contato
Email: thpldevweb@gmail.com

LinkedIn: Tiago Looze

GitHub: THPL28

Licença

Este projeto está licenciado sob os termos da licença MIT. Veja o arquivo LICENSE para mais detalhes.



