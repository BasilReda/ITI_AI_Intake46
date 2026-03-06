from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='products_index'),
    path('<int:pk>/', views.show, name='products_show'),
]
