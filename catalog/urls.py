from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu),
    path('<str:city>/',views.menu),
    path('<int:category>/id<int:ident>/', views.idint),
    path('<str:city>/<int:category>/id<int:ident>/', views.idint)
]
