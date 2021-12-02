from django.urls import path
from rest_framework.decorators import api_view
from .import views

urlpatterns = [
    path('', views.getRoutes),
    path('faults/', views.getFaults),
    path('faults/create/', views.createFault),
    path('faults/<str:pk>/update/', views.updateFault),
    path('faults/<str:pk>/delete/', views.deleteFault),
    path('faults/<str:pk>/', views.getFault),

]