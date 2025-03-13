from django.shortcuts import render
from hospitales.models import ServiceDepartamentos, ServiceHospitales

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

def metodoDepartamentosBBDD(request):
    servicio=ServiceDepartamentos()
    departamentos=servicio.getDepartamentos()
    context={
        "departamentos": departamentos
    }
    return render(request, 'pages/departamentos.html', context)

def metodoHospitalesBBDD(request):
    servicio=ServiceHospitales()
    hospitales=servicio.getHospitales()
    context={
        "hospitales": hospitales
    }
    return render(request, 'pages/hospitales.html', context)

def insertarDepartamento(request):
    if('cajanumero' in request.POST):
        servicio=ServiceDepartamentos()
        numero=request.POST['cajanumero']
        nombre=request.POST['cajanombre']
        localidad=request.POST['cajalocalidad']
        registros= servicio.insertDepartamento(numero, nombre, localidad)
        departamentos=servicio.getDepartamentos()
        context={
            "departamentos": departamentos
        }
        return render(request, 'pages/departamentos.html', context)
    else:
        return render(request, 'pages/insertardepartamento.html')
    
def deleteDepartamento(request):
    if('cajanumero' in request.POST):
        servicio=ServiceDepartamentos()
        numero=request.POST['cajanumero']
        registros= servicio.deleteDepartamento(numero)
        departamentos=servicio.getDepartamentos()
        context={
            "departamentos": departamentos
        }
        return render(request, 'pages/departamentos.html', context)
    else:
        return render(request, 'pages/eliminardepartamento.html')