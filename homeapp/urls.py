from django.urls import path
from homeapp import views

urlpatterns=[
    path('',views.home,name='home'),
    path('birds/', views.birds_view, name='birds'),
    path('birds/<int:pk>/', views.bird_detail_view, name='bird_detail'),
]