from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.utils.translation import gettext_lazy as _


admin.site.site_header = "Accesibility hub"
admin.site.site_title = "Administrator paneel"
admin.site.index_title = "Welkom bij de Administrator paneel"

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'onderzoeker')