from django.contrib import admin
from .models import Incident, Comment

@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = ('description', 'status', 'urgency', 'assigned_to', 'created_at')
    list_filter = ('status', 'urgency', 'created_at')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('incident', 'author', 'text', 'created_at')
    list_filter = ('created_at',)
