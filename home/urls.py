from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page,name='home_page'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('dashboard/<int:uid>/',views.dashboard,name='go_to_dashboard'),
    
]