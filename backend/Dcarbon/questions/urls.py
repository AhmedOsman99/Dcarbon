from django.urls import path
from .views import add_question, get_questions, add_answer

urlpatterns = [
    path('', add_question),
    path('getall', get_questions),
    path('update', add_answer)
]
