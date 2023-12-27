from django.contrib.admin import register, ModelAdmin
from .models import Ticket, Reply

# Register your models here.
@register(Ticket)
class TicketAdmin(ModelAdmin):
    list_display = ['message']

@register(Reply)
class ReplyAdmin(ModelAdmin):
    list_display = ['message']