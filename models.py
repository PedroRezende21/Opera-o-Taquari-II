from django.db import models
from django.contrib.auth.models import User

MARINHA = 'Marinha do Brasil'
EXERCITO = 'Exército Brasileiro'
AERONAUTICA = 'Aeronáutica'

FORCA_CHOICES = [
        (MARINHA, 'Marinha do Brasil'),
        (EXERCITO, 'Exército Brasileiro'),
        (AERONAUTICA, 'Força Aérea'),
    ]

SOLDADO = 'Soldado'
CABO = 'Cabo'
SARGENTO_3 = '3º Sargento'
SARGENTO_2 = '2º Sargento'
SARGENTO_1 = '1º Sargento'
SUB_OFICIAL = 'Sub-Tenente/Sub-Oficial'
TENENTE_2 = '2º Tenente'
TENENTE_1 = '1º Tenente'
CAPITAO = 'Capitão'
MAJOR = 'Capitão de Corveta/Major'
TENENTE_CORONEL = 'Capitão de Fragata/Tenente Coronel'
CORONEL = 'Capitão de Mar e Guerra/Coronel'

POSTO_GRAD_CHOICES = [
        (SOLDADO, 'Soldado'),
        (CABO, 'Cabo'),
        (SARGENTO_3, '3º Sargento'),
        (SARGENTO_2, '2º Sargento'),
        (SARGENTO_1, '1º Sargento'),
        (SUB_OFICIAL, 'Sub-Tenente/Sub-Oficial'),
        (TENENTE_2, '2º Tenente'),
        (TENENTE_1, '1º Tenente'),
        (CAPITAO, 'Capitão'),
        (MAJOR, 'Capitão de Corveta/Major'),
        (TENENTE_CORONEL, 'Capitão de Fragata/Tenente Coronel'),
        (CORONEL, 'Capitão de Mar e Guerra/Coronel'),
    ]
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Adicione campos personalizados aqui
    posto_grad = models.CharField(max_length=100, choices=POSTO_GRAD_CHOICES)
    nome_de_guerra = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username

class Efetivo(models.Model):
    
    forca_armada = models.CharField(max_length=100, choices=FORCA_CHOICES)
    posto_grad = models.ForeignKey(UserProfile.posto_grad, on_delete=models.CASCADE)
    nome_de_guerra = models.ForeignKey(UserProfile.nome_de_guerra, on_delete=models.CASCADE)
    user = models.ForeignKey(User.username, on_delete=models.CASCADE)
    local_da_atividade = models.CharField(max_length=100)
    quantidade_de_pessoal = models.PositiveIntegerField(default=0)
    resgatados = models.PositiveIntegerField(default=0)
    mortos = models.PositiveIntegerField(default=0)




