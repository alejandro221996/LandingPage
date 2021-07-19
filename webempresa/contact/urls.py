from django.urls import path
from . import views

urlpatterns = [
    # paths del contact
    path('', views.contact, name="contact"),
    #path('blog/', views.blog, name="blog"),


]
