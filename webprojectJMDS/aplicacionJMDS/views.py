from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'aplicacionJMDS/index.html')

#    return HttpResponse('Mi primera página django!!!')

def metodoViernes(request):
    return render(request, 'aplicacionJMDS/viernes.html')

def metodoListas(request):
    return render(request, 'aplicacionJMDS/listas.html')
