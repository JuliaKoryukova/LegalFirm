
from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_legal_firm, name='legal_firm'),
]
