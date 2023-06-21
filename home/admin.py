from django.contrib import admin
from django.utils import timezone

from .models import Modelo, Tempo, Etapa, Ordem, Funcionario, osnumero


@admin.register(osnumero)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'numero')


@admin.register(Funcionario)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'contato', 'tipo')
    list_editable = ('nome',)
    list_per_page = 20
    search_fields = ('modelo',)


@admin.register(Modelo)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'modelo')
    list_editable = ('modelo',)
    list_per_page = 20
    search_fields = ('modelo',)

@admin.register(Tempo)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'modelo', 'etapa', 'media')
    list_per_page = 20
    search_fields = ('modelo',)


@admin.register(Ordem)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('numeros', 'status', 'vendedor', 'modelo', 'cliente', 'id', 'tipo', 'prioridade', 'lateral',
                    'conexoes', 'grade', 'bracadeira', 'tampa', 'coxin', 'mangueira', 'colmeia',
                    'data_orcamento', 'data_aprovacao', 'data_entrega'
                    )
    list_filter = ('status', 'tipo', 'vendedor')
    list_per_page = 50
    search_fields = ('numeros', 'cliente',)
    date_hierarchy = 'data_orcamento'
    autocomplete_fields = ['modelo']

    @admin.action(description='Insere etapas')
    def insereEtapas(modeladmin, request, queryset):
        # # buscando id e id do modelo
        # dadosNum = osnumero.objects.get()

        # novoNumero = dadosNum.numero
        # dadosNum.numero = novoNumero
        
        # dadosNum.save()


        for dados in queryset:
            print(dados.base_ptr_id, dados.modelo_id)

        # dados.numeros = novoNumero
        dados.status = '0'
        dados.data_aprovacao = timezone.now()
        dados.save()            

        dadostempo = Tempo.objects.filter(modelo_id=dados.modelo_id)

        for linhas in dadostempo:
            etapa = Etapa()
            etapa.fase = linhas.etapa
            etapa.media = linhas.media
            etapa.id_ordem_id = dados.base_ptr_id
            etapa.os_ordem = dados.numeros
            etapa.save()

    # atualizar Ordem

    actions = [insereEtapas]


@admin.register(Etapa)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = (
    'id', 'os_ordem', 'fase', 'media', 'inicio', 'parada', 'retomada', 'fim', 'decorrido', 'get_tempo_parado', 'operador', 'limpesa', 'conserto', 'caixa_sup',
    'caixa_inf', 'elemento', 'bocal', 'rad_novo', 'colmeia', 'mostrar', 'status'
    )
    list_display_links = ('fase',)
    date_hierarchy = 'inicio'
    list_per_page = 15
    exclude = ('almoco', 'fim_de_turno', 'setup', 'faltaMaterial', 'quebraFerramenta', 'necessidadesPessoais', 'outros')

    def get_tempo_parado(self, obj):
        return obj.controleParado

    get_tempo_parado.short_description = 'Parado'
