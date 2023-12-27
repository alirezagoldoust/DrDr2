from django.http.response import  JsonResponse
from .models import Ticket, Reply


def list_ticket_reply(request):
    replies = Reply.objects.all()
    ans = []
    for item in replies:
        ans.append({
            'ticket': item.ticket.message,
            'reply': item.message,
        })
    return JsonResponse(ans, safe=False)
