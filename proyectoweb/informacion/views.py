from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'informacion/index.html')

def metodoPelis(request):
    return render(request, 'informacion/pelis.html')

def metodoFutbol(request):
    nombre="Real Madrid"
    data={
        "equipo":nombre
    }
    return render(request, 'informacion/futbol.html',data)

def metodoJugadores(request):
    listaJugadores=[
        {
            "Nombre":"Cristiano Ronaldo",
            "Demarcacion":"Delantero",
            "Numero": 7
        },
        {
            "Nombre": "Guti",
            "Demarcacion": "Centrocampista",
            "Numero": 14
        },
        {
            "Nombre": "Karim Benzema",
            "Demarcacion": "Delantero",
            "Numero":9
        },
        {
            "Nombre": "Toni Kroos",
            "Demarcacion": "Centrocampista",
            "Numero":8
        },
        {
            "Nombre": "Thibaut Courtois",
            "Demarcacion": "Portero",
            "Numero": 1
        }
    ]

    context = {
        "jugadores": listaJugadores
    }
    return render(request, 'informacion/jugadores.html',context)

def metodoColores(request):
    if ('micolor' in request.GET):
        colorRecibido=request.GET['micolor']
        context={
            "colordibujo": colorRecibido
        }
        return render(request, 'informacion/colores.html',context)
    else:
        return render(request, 'informacion/colores.html')
    
def metodoSaludo(request):
    if ('cajanombre' in request.POST):
        nombrerRecibido=request.POST['cajanombre']
        context={
            "nombre": nombrerRecibido
        }
        return render(request, 'informacion/saludo.html', context)
    else:
        return render(request, 'informacion/saludo.html')
    
def metodoSumarNumeros(request):
    if ('cajanumero1' in request.POST):
        num1=request.POST['cajanumero1']
        num2=request.POST['cajanumero2']
        suma=int(num1)+int(num2)
        context={
            "suma": suma,
            "numero1": num1,
            "numero2": num2
        }
        return render(request, 'informacion/sumarnumeros.html', context)
    else:
        return render(request, 'informacion/sumarnumeros.html')
    
def metodoCollatz(request):
    if ('cajanumero' in request.POST):
        dato=request.POST['cajanumero']
        numero=int(dato)
        listanumeros=[]
        while(numero!=1):
            if (numero % 2 ==0):
                numero=int(numero/2)
            else:
                numero=int(numero*3+1)
            listanumeros.append(numero)
        context={
            "numeroscollatz": listanumeros
            }
        return render(request, 'informacion/collatz.html', context)
    else:
        return render(request, 'informacion/collatz.html')

def metodoTablaMultiplicar(request):
    if ('cajanumero' in request.POST):
        dato = request.POST['cajanumero']
        numero = int(dato)
        listaTabla = []
        for i in range(10):
            resultado=numero*(i+1)
            operacion=str(numero) + " * " + str((i+1))
            listaTabla.append({
                "operacion": operacion
                "resultado": resultado
            })
        context = {
            "listatabla": listaTabla
            }
        return render(request, 'informacion/tabla.html', context)
    else:
        return render(request, 'informacion/tabla.html')