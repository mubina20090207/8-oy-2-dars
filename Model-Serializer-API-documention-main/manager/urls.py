from django.urls import path

from .views import *

urlpatterns = [
    path('class/', KlassView.as_view()),
    path('class/<int:pk>/', KlassView.as_view()),

    path('hotel/', HotelView.as_view()),
    path('hotel/<int:pk>/', HotelView.as_view()),

    path('travel/', TravelView.as_view()),
    path('travel/<int:pk>/', TravelView.as_view()),
]