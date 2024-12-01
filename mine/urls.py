from django.urls import path
from .import views

urlpatterns = [
    
    path('',views.home , name="home"),

    path('article/<int:pk>',views.singuler_article,name="article"),

]
