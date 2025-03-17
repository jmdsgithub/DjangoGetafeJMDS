from django.urls import path
from hospitales import views

urlpatterns=[
    path('', views.index, name='index'),
    path('departamentos/', views.metodoDepartamentosBBDD, name='departamentos'),
    path('hospitales/', views.metodoHospitalesBBDD, name='hospitales'),
    path('insertardepartamento/', views.insertDepartamento, name='insertardepartamento'),
    path('eliminardepartamento/', views.eliminarDepartamento, name='eliminardepartamento'),
    path('detallesdepartamento/', views.detallesDepartamento, name='detallesdepartamento'),
    path('modificardepartamento/', views.modificarDepartamento, name='modificardepartamento'),
    path('empleadosdepartamento/', views.empleadosDepartamento, name='empdept')
]
