from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='principal'),
    path('citas/',views.citas, name='citas'),
]