from django.urls import path
from . import views
from .views import feedback_view
urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('productCard/<int:product_id>/', views.productCard, name='productCard'), 
    path('katalog', views.katalog, name='catalog'),
    path('kontact', views.kontact),
    path('feedback/', feedback_view, name='feedback'),
    path('make_order/', views.make_order, name='make_order'),
]