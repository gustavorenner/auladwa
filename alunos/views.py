from django.shortcuts import render
from.models import Aluno

def index(request):
    def detalhes_aluno(request, aluno_id):
    aluno = Aluno.objects.get(id=aluno_id)
    return render(request, 'alunos/detalhes_aluno.html', {'aluno': aluno})

