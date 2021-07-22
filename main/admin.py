from django.contrib import admin
from main.models import Partenaire, Avantage, Plugin, Accueil, Prestation, Studio, Site

# Register your models here.
@admin.register(Partenaire)
class PartenaireAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    search_fields = ('name',)

@admin.register(Avantage)
class AvantageAdmin(admin.ModelAdmin):
    list_display = ('text', 'id')
    search_fields = ('name',)

@admin.register(Plugin)
class PluginAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    search_fields = ('name',)

@admin.register(Accueil)
class AccueilAdmin(admin.ModelAdmin):
    list_display = ('name', 'titre', 'id')
    search_fields = ('name',)

@admin.register(Prestation)
class PrestationAdmin(admin.ModelAdmin):
    list_display = ('name', 'titre', 'id')
    search_fields = ('name',)

@admin.register(Studio)
class StudioAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    search_fields = ('name',)

@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False