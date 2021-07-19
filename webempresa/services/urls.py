from django.urls import path
from . import views

urlpatterns = [
    # paths del admin
    path('', views.services, name="services"),

]
