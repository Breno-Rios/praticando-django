from django.contrib import admin
from galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "name", "legenda")
    list_display_links = ("id","name")
    search_fields = ('name',)


admin.site.register(Fotografia, ListandoFotografias)
