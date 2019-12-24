from django.urls import path

from . import views

urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('<int:pk>/', views.mission, name='mission'),
    path('<int:pk>/results/', views.return_results_page, name='results'),
    path('<int:pk>/ajax/next_word/', views.next_word, name='next_word'),
    path('<int:pk>/ajax/check_answer/', views.check_answer, name='check_answer'),
    path('ans/', views.get_answers, name='ans'),
]
