from rest_framework import viewsets, generics
from .serializer import CursoSerializer, DisciplinaSerializer, TurmaSerializer, ProfessorSerializer, \
    PeriodoLetivoSerializer, EqualizacaoSerializer, ListaProfessorEqualizacaoSerializer, \
    ListaDisciplinaEqualizacaoSerializer, ListaPeriodoLetivoEqualizacaoSerializer
from .models import Professor, Disciplina, Turma, Equalizacao, PeriodoLetivo, Curso
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class CursosViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class TurmasViewSet(viewsets.ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class DisciplinasViewSet(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class ProfessoresViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class PeriodoLetivoViewSet(viewsets.ModelViewSet):
    queryset = PeriodoLetivo.objects.all()
    serializer_class = PeriodoLetivoSerializer


class EqualizacaoViewSet(viewsets.ModelViewSet):
    queryset = Equalizacao.objects.all()
    serializer_class = EqualizacaoSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class ListaProfessorEqualizacao(generics.ListAPIView):
    def get_queryset(self):
        queryset = Equalizacao.objects.filter(professor_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListaProfessorEqualizacaoSerializer
    # authentication_classes = [BasicAuthentication]


class ListaDisciplinaEqualizacao(generics.ListAPIView):
    def get_queryset(self):
        queryset = Equalizacao.objects.filter(disciplina_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListaDisciplinaEqualizacaoSerializer


class ListaPeriodoLetivoEqualizacao(generics.ListAPIView):
    def get_queryset(self):
        queryset = Equalizacao.objects.filter(disciplina_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListaPeriodoLetivoEqualizacaoSerializer


"""
def exportar_csv(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['Nome', 'Email', 'Carga Horaria Alocada'])

    for equalizacao in Equalizacao.objects.all().values_list('nome_completo', 'email', 'carga_horaria_alocada'):
        writer.writerow(equalizacao)

    response['Content-Disposition'] = 'attachment; filename="professores-esu.csv"'

    return response
"""
