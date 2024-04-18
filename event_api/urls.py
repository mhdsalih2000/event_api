from django.urls import path
from .views import create_csv,AsyncView



urlpatterns = [
    path('create',create_csv.as_view()),
    path('find',AsyncView.as_view({'get': 'get'}))



]