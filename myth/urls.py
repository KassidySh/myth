from django.urls import path
from . import views

urlpatterns = [
    path('', views.region_list, name='region_list'),
    path('type/', views.type_list, name='type_list'),
    path('type/<int:pk>/', views.single_type, name='single_type'),
    path('region/<int:pk>/', views.single_region, name='single_region'),
    path('god/<int:pk>/', views.single_being, name='single_being'),
    # SHOULD AUTO CHOOSE GOD
    path('story/new/<int:pk>/', views.new_story, name='new_story'),
    path('story/<int:pk>/edit/', views.edit_story, name='edit_story'),
    path('story/<int:pk>/<int:god_pk>/delete', views.delete_story, name='delete_story'),
    #Add comments
    path('comment/new/<int:pk>/<int:god_pk>', views.new_comment, name='new_comment'),
    path('comment/<int:pk>/<int:god_pk>/edit/', views.edit_comment, name='edit_comment'),
    path('comment/<int:pk>/<int:god_pk>/delete', views.delete_comment, name='delete_comment'),
    #Favorite Stories and Favorite Gods
]