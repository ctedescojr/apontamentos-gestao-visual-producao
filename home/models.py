from django.db import models
from django.contrib.auth.models import User



class Base(models.Model):
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)


class Modelo(models.Model):
    modelo = models.CharField(max_length=150)

    class Meta:
        ordering = ['modelo']

    def __str__(self):
        return self.modelo

class osnumero(models.Model):

    class Meta:
        verbose_name_plural = 'OS Números'

    numero = models.IntegerField()


class Tempo(models.Model):
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    etapa = models.CharField(choices=(
        ('1', 'Etapa Um'),
        ('2', 'Etapa Dois'),
        ('3', 'Etapa Três'),
    ), max_length=1)
    media = models.IntegerField()

    def __str__(self):
        return 'Tempo'


class Funcionario(Base):

    class Meta:
        verbose_name_plural = 'Funcionários'
        ordering = ['nome']

    nome = models.CharField(max_length=60)
    contato = models.CharField(max_length=15)
    tipo = models.CharField(choices=(
        ('V', 'Vendedor'),
        ('O', 'Operador'),
    ), max_length=1)

    def __str__(self):
        return self.nome

class Ordem(Base):

    class Meta:
        verbose_name_plural = 'Ordens'
    
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    cliente = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    numeros = models.IntegerField(default=1)
    tem_acessorio = models.BooleanField(default=False)
    tipo = models.CharField(choices=(
        ('N', 'Nova'),
        ('R', 'Retrabalho'),
        ('G', 'Garantia'),
        ('2', 'Outro'),
    ), max_length=1)
    orcamento = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    data_orcamento = models.DateTimeField(auto_now_add=True)
    data_aprovacao = models.DateTimeField(auto_now_add=True)
    data_entrega = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=(
        ('0', 'inciada'),
        ('1', 'Andamento'),
        ('2', 'Aguardando'),
        ('3', 'Finalizada'),
        ('4', 'Pendente de Abertura')
    ), max_length=1, default='4')
    prioridade = models.IntegerField(default=1)
    lateral = models.IntegerField(default=0)
    defletor = models.IntegerField(default=0)
    conexoes = models.IntegerField(default=0)
    grade = models.IntegerField(default=0)
    bracadeira = models.IntegerField(default=0)
    tampa = models.IntegerField(default=0)
    coxin = models.IntegerField(default=0)
    mangueira = models.IntegerField(default=0)
    colmeia = models.IntegerField(default=0)
    obs_ordem = models.TextField(default='Nada')

    def save(self, *args, **kwargs):
        if not self.pk:  # Verifica se é uma nova instância de Ordem
            ultimo_numero_os = osnumero.objects.last()
            if ultimo_numero_os:
                self.numeros = ultimo_numero_os.numero + 1
                ultimo_numero_os.numero = self.numeros
                ultimo_numero_os.save()
            else:
                self.numeros = 1
                osnumero.objects.create(numero=self.numeros)
        super().save(*args, **kwargs)

    @classmethod
    def get_default_numeros(cls):
        ultimo_numero_os = osnumero.objects.last()
        if ultimo_numero_os:
            return ultimo_numero_os.numero + 1
        return 1

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._meta.get_field('numeros').default = self.get_default_numeros

class Etapa(Base):
    id_ordem = models.ForeignKey(Ordem, on_delete=models.CASCADE, editable=False)
    os_ordem = models.IntegerField(default=0)
    operador = models.ForeignKey(Funcionario, on_delete=models.CASCADE, default=3)
    fase = models.CharField(choices=(
        ('1', 'Fase1'),
        ('2', 'Fase2'),
        ('3', 'Fase3'),
    ), max_length=1)
    media = models.IntegerField()
    inicio = models.DateTimeField(blank=True, null=True)
    parada = models.DateTimeField(blank=True, null=True)
    retomada = models.DateTimeField(blank=True, null=True)
    fim = models.DateTimeField(blank=True, null=True)
    decorrido = models.IntegerField(default=0)
    quantidadeParadas = models.IntegerField(default=0, verbose_name='Quantiadade de Paradas')
    parado = models.IntegerField(default=0, verbose_name='Total Parado Bruto')
    controleParado = models.IntegerField(default=0, verbose_name='Total Parado Efetivo')
    limpesa = models.CharField(choices=(
        ('S', 'Sim'),
        ('N', 'Não'),
    ), max_length=1, default='N')
    conserto = models.CharField(choices=(
        ('S', 'Sim'),
        ('N', 'Não'),
    ), max_length=1, default='N')
    caixa_sup = models.CharField(choices=(
        ('S', 'Sim'),
        ('N', 'Não'),
    ), max_length=1, default='N')
    caixa_inf = models.CharField(choices=(
        ('S', 'Sim'),
        ('N', 'Não'),
    ), max_length=1, default='N')
    elemento = models.CharField(choices=(
        ('S', 'Sim'),
        ('N', 'Não'),
    ), max_length=1, default='N')
    bocal = models.CharField(choices=(
        ('S', 'Sim'),
        ('N', 'Não'),
    ), max_length=1, default='N')
    rad_novo = models.CharField(choices=(
        ('S', 'Sim'),
        ('N', 'Não'),
    ), max_length=1, default='N')
    colmeia = models.CharField(choices=(
        ('S', 'Sim'),
        ('N', 'Não'),
    ), max_length=1, default='N')
    mostrar = models.CharField(choices=(
        ('1', 'Sim'),
        ('0', 'Não'),
        ('2', 'Ativo'),
    ), max_length=1, default='0')
    status = models.CharField(choices=(
        ('0', 'Aberto'),
        ('1', 'Executando'),
        ('6', 'Aguardando'),
        ('8', 'Parado'),
        ('2', 'Retomar'),
        ('3', 'Final'),
    ), max_length=1, default='0')
    obs_etapa = models.TextField(default='Nada')
    almoco = models.IntegerField(default=0)
    fim_de_turno = models.IntegerField(default=0)
    setup = models.IntegerField(default=0)
    faltaMaterial = models.IntegerField(default=0)
    quebraFerramenta = models.IntegerField(default=0)
    necessidadesPessoais = models.IntegerField(default=0)
    outros = models.IntegerField(default=0)