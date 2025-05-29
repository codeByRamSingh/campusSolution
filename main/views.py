from django.http import HttpResponse

def landing(request):
    return HttpResponse("Hello World")