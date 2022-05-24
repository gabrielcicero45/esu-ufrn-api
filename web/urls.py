from django.urls import path, include
#from .views import cadastrar_professor, listar_professores, editar_professor, remover_professor, exportar_csv

urlpatterns = [
    path('', include('web.urls')),
]