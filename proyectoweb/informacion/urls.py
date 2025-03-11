from django.urls import path
from informacion import views

urlpatterns=[
    path('', views.index, name='index'),
    path('pelis/', views.metodoPelis, name='pelis'),
    path('futbol/', views.metodoFutbol, name='futbol'),
    path('jugadores/', views.metodoJugadores, name='jugadores'),
    path('colores/', views.metodoColores, name='colores'),
    path('saludo/', views.metodoSaludo, name='saludo'),
    path('sumarnumeros/', views.metodoSumarNumeros, name='sumarnumeros')
]