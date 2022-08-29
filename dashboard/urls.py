from django.urls import path
from . import views

urlpatterns = [
    path('add_question/<int:uid>',views.add_question,name='add_question'),
    path('add_vote/<int:uid>/',views.add_vote,name='add_vote'),
     path('view_profile/<int:uid>/',views.view_profile,name='view_profile')
]