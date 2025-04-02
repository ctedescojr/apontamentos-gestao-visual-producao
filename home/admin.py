from django.contrib import admin

from .models import Modelo, Tempo, Etapa, Ordem, Funcionario, osnumero


@admin.register(osnumero)
class OSNumeroAdmin(admin.ModelAdmin):
    list_display = ("id", "numero")


@admin.register(Funcionario)
class Funcionarioadmin(admin.ModelAdmin):
    list_display = ("id", "nome", "contato", "tipo")
    list_editable = ("nome",)
    list_per_page = 20
    search_fields = ("modelo",)


@admin.register(Modelo)
class ModeloAdmin(admin.ModelAdmin):
    list_display = ("id", "modelo")
    list_editable = ("modelo",)
    list_per_page = 20
    search_fields = ("modelo",)


@admin.register(Tempo)
class TempoAdmin(admin.ModelAdmin):
    list_display = ("id", "modelo", "etapa", "media")
    list_per_page = 20
    search_fields = ("modelo",)


@admin.register(Ordem)
class OrdemAdmin(admin.ModelAdmin):
    list_display = (
        "numeros",
        "status",
        "vendedor",
        "modelo",
        "cliente",
        "id",
        "tipo",
        "prioridade",
        "lateral",
        "conexoes",
        "grade",
        "bracadeira",
        "tampa",
        "coxin",
        "mangueira",
        "colmeia",
        "data_orcamento",
        "data_aprovacao",
        "data_entrega",
    )
    list_filter = ("status", "tipo", "vendedor")
    list_per_page = 50
    search_fields = ("numeros", "cliente")
    date_hierarchy = "data_orcamento"
    autocomplete_fields = ["modelo"]

    def save_model(self, request, obj, form, change):
        """Verifica se o status foi alterado para 'Iniciada' e adiciona as etapas."""
        if change:  # Apenas se a ordem já existir (não é nova)
            ordem_antiga = Ordem.objects.get(pk=obj.pk)
            if ordem_antiga.status != "0" and obj.status == "0":
                self.insereEtapas(request, [obj])

        super().save_model(request, obj, form, change)

    @admin.action(description="Insere etapas")
    def insereEtapas(self, request, queryset):
        """Cria as etapas associadas às ordens selecionadas."""
        for dados in queryset:
            dadostempo = Tempo.objects.filter(modelo_id=dados.modelo_id)

            for tempo in dadostempo:
                Etapa.objects.create(
                    id_ordem=dados,
                    os_ordem=dados.numeros,
                    fase=tempo.etapa,
                    media=tempo.media,
                    status="0",
                )

    actions = [insereEtapas]  # Permite execução manual


@admin.register(Etapa)
class EtapaAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "os_ordem",
        "fase",
        "media",
        "inicio",
        "parada",
        "retomada",
        "fim",
        "decorrido",
        "get_tempo_parado",
        "operador",
        "limpesa",
        "conserto",
        "caixa_sup",
        "caixa_inf",
        "elemento",
        "bocal",
        "rad_novo",
        "colmeia",
        "mostrar",
        "status",
    )
    list_display_links = ("fase",)
    date_hierarchy = "inicio"
    list_per_page = 15
    exclude = (
        "almoco",
        "fim_de_turno",
        "setup",
        "faltaMaterial",
        "quebraFerramenta",
        "necessidadesPessoais",
        "outros",
    )

    def get_tempo_parado(self, obj):
        return obj.controleParado

    get_tempo_parado.short_description = "Parado"
