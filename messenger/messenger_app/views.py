from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Message

# Create your views here.
def index(request: HttpRequest):
    return HttpResponse('Index page')

@csrf_exempt # DELETE THEN
def set_message(request: HttpRequest):
    if request.method == 'POST':
        print('+++++++POST')
        print(request.body)
    return HttpResponse('message')

def view_all_messages(request: HttpRequest):
    messages = Message.objects.order_by('-created_at')
    context = {
            "messages": messages,
            'title': 'Messages'
        }
    return render(request, 'messenger_app/view_all_messages.html', context)
 