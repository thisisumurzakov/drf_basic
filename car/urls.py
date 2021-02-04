from django.urls import path
from .views import *

urlpatterns = [
    path('car_create/', CarCreateView.as_view()),
    path('all/', CarListView.as_view()),
    path('car_detail/<int:pk>/', CarDetailView.as_view()),

]
