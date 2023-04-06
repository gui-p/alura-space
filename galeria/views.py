from django.shortcuts import render

# request é o endereço requisitado, o segundo argumento é o arquivo localizado em "templates"
def index(request):
    return render(request, 'index.html')