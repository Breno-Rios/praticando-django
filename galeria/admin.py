from django.contrib import admin
from galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "name", "legenda","publicada")
    list_display_links = ("id","name")
    search_fields = ('name',)
    list_filter = ('categoria',)
    list_editable = ("publicada",)
    list_per_page = 10


admin.site.register(Fotografia, ListandoFotografias)
