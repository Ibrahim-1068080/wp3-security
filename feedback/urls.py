from django.urls import path
from . import views

urlpatterns = [
    path('feedback/', views.feedback_view, name='feedback'),
    path('feedback/thanks/', views.feedback_thanks, name='feedback_thanks'),
    path('view-feedback/', views.view_feedback, name='view_feedback'),
    # Voeg andere paden toe zoals nodig
]
