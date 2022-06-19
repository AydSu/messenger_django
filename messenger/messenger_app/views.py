from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request: HttpRequest):
    return HttpResponse('Index page')

@csrf_exempt # DELETE THEN
def view_message(request: HttpRequest):
    if request.method == 'POST':
        print('+++++++POST')
        print(request.body)
    return HttpResponse('message')