from django.urls import path
from .views import *

urlpatterns = [
    path('add_question/<int:uid>/',QuestionAPI.as_view()),
    path('get_questions/',QuestionAPI.as_view()),
    path('delete_24_hrs_old_questions/',QuestionAPI.as_view()),
    path('get_questions/<int:uid>/',UserQuestion.as_view()),
    
    path('add_vote/<int:uid>/',AddVote.as_view()),
]