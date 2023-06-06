from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    #ex: /polls/
    path('', views.IndexView.as_view(), name = 'index'),
    #ex: /polls/detail/question_id/
    path("detail/<int:pk>/", views.DetailView.as_view(), name="detail"),
    #ex: /polls/results/question_id/
    path("results/<int:pk>/", views.ResultView.as_view(), name="results"),
    #ex: /polls/vote/question_id/
    path("vote/<int:question_id>/", views.vote, name="vote"),
]