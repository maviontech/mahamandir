from django.contrib import admin
from .models import ContactMessage, Subscriber


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at']
    search_fields = ['name', 'email', 'message']
    list_filter = ['created_at']


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['email', 'created_at']
    search_fields = ['email']
