from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse # remove this import later


# remove this function later:
def starter_home(request):
    return HttpResponse("<h1>HOME PAGE</h1>")


urlpatterns = [
    path('', starter_home, name='home'),
    path('admin/', admin.site.urls),
    path('authentication/', include('authentication.urls')),
]
