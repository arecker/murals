from django.contrib import admin

from models import Message


class MessageAdmin(admin.ModelAdmin):
    model = Message


admin.site.register(Message, MessageAdmin)
