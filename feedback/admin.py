from django.contrib import admin
from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'name', 'experience')

admin.site.register(Feedback, FeedbackAdmin)
