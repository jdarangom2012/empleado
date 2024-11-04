from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.IndexView.as_view()),
    path('lista/', views.PruebaListView.as_view()),
    path('listaprueba/', views.ModeloPruebaListView.as_view()),   
    path('add/', views.PruebaCreateListView.as_view(),name='prueba_add'),   
    path(
        'resumen-foundation-view/', 
        views.ResumenFoundationView.as_view(),
        name='resumen_foundation_view'
        ), 
    
]
