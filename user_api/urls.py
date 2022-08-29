from django.urls import path
from .views import *

urlpatterns = [
    path('save_user/',UserAPI.as_view()),
    path('login_user/',UserLogin.as_view()),
    path('get_user_info/<int:uid>/',UserLogin.as_view())
]
