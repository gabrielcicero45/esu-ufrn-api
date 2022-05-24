from django.db import models


# Create your models here.
class Curso(models.Model):
    CURSOS_ESU = [
        ('TRIS', 'Técnico em Registros e Informações em Saúde'),
        ('TENF', 'Tecnico em Enfermagem '),
        ('VISAU', 'Técnico em Vigilância em Saúde'),
        ('MASSO', 'Tecnico em Massoterapia'),
        ('TACS', 'Técnico Agente Comunitário em Saúde'),
        ('GH', 'Gestão Hospitalar'),
        ('MP', 'Mestrado Profissional')
    ]
    nome = models.CharField(max_length=5, null=False, blank=False, choices=CURSOS_ESU, default='TRIS')
    def __str__(self):
        return self.nome


class Professor(models.Model):
    nome_completo = models.CharField(max_length=100, null=False, blank=False)
    # email = models.EmailField(null=False, blank=False,unique=True)
    carga_horaria_alocada = models.IntegerField(default=0, null=False)

    def __str__(self):
        return self.nome_completo


class Disciplina(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    codigo = models.CharField(max_length=10, null=False, blank=False, unique=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    carga_horaria = models.IntegerField(default=0, null=False)

    def __str__(self):
        return self.nome


class Turma(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    capacidade = models.IntegerField(default=0, null=False)

    def __str__(self):
        return self.nome

class PeriodoLetivo(models.Model):
    descricao = models.CharField(max_length=10, null=False, blank=False)
    dataInicio = models.DateField(auto_now=False, auto_now_add=False)
    dataFim = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.descricao

class Equalizacao(models.Model):
    periodoLetivo = models.ForeignKey(PeriodoLetivo, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    carga_horaria = models.IntegerField(default=0, null=False)
