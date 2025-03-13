from django.urls import path
from hospitales import views

urlpatterns=[
    path('', views.index, name='index'),
    path('departamentos/', views.metodoDepartamentosBBDD, name='departamentos'),
    path('hospitales/', views.metodoHospitalesBBDD, name='hospitales'),
    path('insertardepartamento/', views.insertarDepartamento, name='insertardepartamento'),
    path('eliminardepartamento/', views.eliminarDepartamento, name='eliminardepartamento'),
]
