from rest_framework import serializers
from .models import Turma, Disciplina, Professor, Equalizacao, Curso, PeriodoLetivo


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = "__all__"


class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = "__all__"


class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = "__all__"


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = "__all__"

class PeriodoLetivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodoLetivo
        fields = "__all__"

class EqualizacaoSerializer(serializers.ModelSerializer):
    periodo_letivo_nome = serializers.ReadOnlyField(source='periodo_letivo.descricao')
    turma_nome = serializers.ReadOnlyField(source='turma.nome')
    professor_nome = serializers.ReadOnlyField(source='professor.nome_completo')
    disciplina_nome = serializers.ReadOnlyField(source='disciplina.nome')
    class Meta:
        model = Equalizacao
        fields = "__all__"


class ListaProfessorEqualizacaoSerializer(serializers.ModelSerializer):
    turma_nome = serializers.ReadOnlyField(source='turma.nome')
    professor_nome = serializers.ReadOnlyField(source='professor.nome_completo')
    disciplina_nome = serializers.ReadOnlyField(source='disciplina.nome')

    class Meta:
        model = Equalizacao
        fields = ['id','turma_nome', 'professor_nome', 'disciplina_nome', 'carga_horaria']


class ListaDisciplinaEqualizacaoSerializer(serializers.ModelSerializer):
    turma_nome = serializers.ReadOnlyField(source='turma.nome')
    professor_nome = serializers.ReadOnlyField(source='professor.nome_completo')
    disciplina_nome = serializers.ReadOnlyField(source='disciplina.nome')

    class Meta:
        model = Equalizacao
        fields = ['id','turma_nome', 'professor_nome', 'disciplina_nome','carga_horaria']

class ListaPeriodoLetivoEqualizacaoSerializer(serializers.ModelSerializer):
    turma_nome = serializers.ReadOnlyField(source='turma.nome')
    professor_nome = serializers.ReadOnlyField(source='professor.nome_completo')
    disciplina_nome = serializers.ReadOnlyField(source='disciplina.nome')

    class Meta:
        model = Equalizacao
        fields = ['id', 'turma_nome', 'professor_nome', 'disciplina_nome', 'carga_horaria']