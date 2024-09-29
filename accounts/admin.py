from django.contrib import admin
from .models import Ervaringsdeskundige, Onderzoek, Organisatie
from .models import Bericht
from .models import Onderzoek, Deelname
import uuid


@admin.register(Ervaringsdeskundige)
class ErvaringsdeskundigeAdmin(admin.ModelAdmin):
    list_display = ['gebruiker', 'is_verified']
    actions = ['verify_users']

    def verify_users(self, request, queryset):
        queryset.update(is_verified=True)
    verify_users.short_description = "Ervaringsdeskunige verifieren"

@admin.register(Onderzoek)
class OnderzoekAdmin(admin.ModelAdmin):
    list_display = ('titel', 'datum_vanaf', 'datum_tot', 'met_beloning', 'is_verified')
    list_filter = ('met_beloning', 'datum_vanaf')
    search_fields = ('titel', 'beschrijving')
    actions = ['verify_users']

    def verify_users(self, request, queryset):
        queryset.update(is_verified=True)
        self.message_user(request, "Geselecteerde onderzoeken zijn succesvol geverifieerd.")
    verify_users.short_description = "Verifieer geselecteerde onderzoeken."

@admin.register(Organisatie)
class OrganisatieAdmin(admin.ModelAdmin):
    list_display = ['naam', 'email', 'api_key', 'is_verified']
    actions = ['generate_api_keys', 'clear_api_keys', 'verify_users']

    def verify_users(self, request, queryset):
        queryset.update(is_verified=True)
        self.message_user(request, "geselecteerde organisaties zijn succesvol geverifieerd.")
    verify_users.short_description = "bevestig geselecteerde organisatie"

    def generate_api_keys(self, request, queryset):
        for organisatie in queryset:
            organisatie.api_key = uuid.uuid4()
            organisatie.save()
        self.message_user(request, "API Keys zijn succesvol gecreeerd voor de geselecteerde Organisaties.")
    generate_api_keys.short_description = "Genereer API keys voor de geselecteerde organisaties."

    def clear_api_keys(self, request, queryset):
        queryset.update(api_key=None)
        self.message_user(request, "API keys succesvol verwijdeer successfully voor de geselecteerde organisaties.")

    clear_api_keys.short_description = "Verwijder API keys voor de geselecteerde organisaties"

@admin.register(Bericht)
class BerichtAdmin(admin.ModelAdmin):
    list_display = ['onderwerp', 'afzender', 'ontvanger', 'verzenddatum', 'gelezen']
    list_filter = ['gelezen', 'verzenddatum']
    search_fields = ['onderwerp', 'bericht', 'afzender__username', 'ontvanger__username']

class DeelnameAdmin(admin.ModelAdmin):
    list_display = ('onderzoek', 'gebruiker', 'datum_deelname')
    list_filter = ('onderzoek', 'gebruiker')
    search_fields = ('onderzoek__titel', 'gebruiker__username')
    
admin.site.register(Deelname, DeelnameAdmin)