from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('cars/', views.cars, name='cars'),
    path('cars/details/<int:id>/', views.details, name='details'),
    path('cars/create/', views.create_car, name='create_car'),
    path('cars/edit/<int:id>/', views.edit_car, name='edit_car'),  # Add this line
    path('cars/delete/<int:id>/', views.delete_car, name='delete_car'),  # Add this line
    path('testing/', views.testing, name='testing'),
]
