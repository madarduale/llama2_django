
from django.urls import path
from .views import index, ask_question

urlpatterns = [
    # path('home/', index, name='index'),
    path('', ask_question, name='ask_question'),
]
