from django.shortcuts import render
from django.http import HttpResponse

# caso chame a pagina inicial vai cair em templates/index.html
def index(request):
        return render(request, 'galeria/index.html')

def imagem(request):
        return render(request, 'galeria/imagem.html')