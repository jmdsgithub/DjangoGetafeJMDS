from django.urls import path
from aplicacion import views

#todo lo que vaya por la web 'app' entra por esas dos comillas vacías q están allí en path
urlpatterns=[
    path('', views.index, name='index'),
    path('listas/', views.metodoListas, name='listas'),
    path('viernes/', views.metodoViernes, name='viernes')
]
