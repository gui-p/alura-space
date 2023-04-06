from django.shortcuts import render

# request é o endereço requisitado, o segundo argumento é o arquivo localizado em "templates"
def index(request):
    return render(request, 'galeria/index.html')

def imagem(request):
    return render(request, "galeria/imagem.html")

def surpreso(request):
    return render (request, "galeria/surpresa.html")