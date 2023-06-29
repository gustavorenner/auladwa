from django.shortcuts import render


from django.urls import path
from . import views

urlpatterns = [
    # ... outras rotas
    path('contato/', views.contato_form, name='contato'),
    # ... outras rotas
]

def contato_form(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem = request.POST.get('mensagem')
        
        # Simule o envio do e-mail exibindo as informações no terminal
        print(f'Nome: {nome}')
        print(f'E-mail: {email}')
        print(f'Mensagem: {mensagem}')

        return render(request, 'contato/confirmacao.html')
    else:
        return render(request, 'contato/formulario.html')
