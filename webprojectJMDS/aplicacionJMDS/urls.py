from django.urls import path

from aplicacionJMDS import views

urlpatterns=[
    path('', views.index, name='index')
    path('viernes/', views.metodoViernes, name='viernes'),
    path('listas/', views.metodoListas, name='listas')
]
