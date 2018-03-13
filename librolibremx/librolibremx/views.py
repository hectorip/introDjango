from django.http import HttpResponse


def home(request):
    return HttpResponse("<title>home</title>")