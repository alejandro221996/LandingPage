from django.urls import path
from . import views

urlpatterns = [
    # paths del admin
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    #path('services/', views.services, name="services"),
    path('store/', views.store, name="store"),

    #path('blog/', views.blog, name="blog"),


]
