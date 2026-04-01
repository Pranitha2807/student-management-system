from django.urls import path
from . import views

urlpatterns = [
    path('', views.carousel_view),
]