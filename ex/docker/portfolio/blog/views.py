from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    msg = 'My Message'
    return render(request, 'blog/index.html', {'message':msg})