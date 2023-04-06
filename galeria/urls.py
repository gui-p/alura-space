from django.urls import path
from galeria.views import index, imagem, surpreso

urlpatterns = [
    path('', index, name='index'),
    path('imagem/', imagem, name='imagem'),
    path('surpresa/', surpreso, name='surpreso')
]