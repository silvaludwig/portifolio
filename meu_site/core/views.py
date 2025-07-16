from django.shortcuts import render
from datetime import datetime

def home(request):
    imagens = [
        {'url': '/media/galeria/lud-bastidores-pb.jpg'},
        {'url': '/media/galeria/lud-violao-1.jpg'},
        {'url': '/media/galeria/lud-piano-2-pb.jpg'},
        # Adicione quantas quiser
    ]
    return render(request, 'home.html', {'imagens': imagens, 'year': datetime.now().year})

def aula_online(request):
    return render(request, 'aula_online.html', {'year': datetime.now().year})

def aula_presencial(request):
    return render(request, 'aula_presencial.html', {'year': datetime.now().year})

def contato(request):
    return render(request, 'contato.html', {'year': datetime.now().year})


def eventos(request):
    return render(request, 'eventos.html', {'year': datetime.now().year})

def sobre(request):
    return render(request, 'sobre.html', {'year': datetime.now().year})