from django.contrib import admin
from .models import Message
# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'created_at', 'updated_at', 'read_flag')
    list_display_links = ('id', 'text')


admin.site.register(Message, MessageAdmin)
