from django.http import HttpResponse


def authentication_starter(request):
    return HttpResponse("<h1>AUTHENTICATION PAGE</h1>")
