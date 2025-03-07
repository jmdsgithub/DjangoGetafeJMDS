from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'aplicacion/index.html')

#    return HttpResponse('Mi primera página django!!!')

def metodoViernes(request):
    return render(request, 'aplicacion/viernes.html')

def metodoListas(request):
    return render(request, 'aplicacion/listas.html')


#    return HttpResponse('Hoy es viernes!!!!!')
