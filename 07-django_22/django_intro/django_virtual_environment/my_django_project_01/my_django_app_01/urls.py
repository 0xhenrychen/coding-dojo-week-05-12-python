from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('<first_name>', views.first_name)
]