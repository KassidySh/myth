from django.urls import path
from . import views

urlpatterns = [
    path('', views.region_list, name='region_list'),
    path('type/', views.type_list, name='type_list'),
    path('type/<int:pk>', views.single_type, name='single_type'),
    path('region/<int:pk>', views.single_region, name='single_region'),
    path('god/<int:pk>', views.single_being, name='single_being'),
]