from django.urls import path
from tasks import views

urlpatterns = [
    path('', views.index, name='home'),
    path('delete/<str:pk>/', views.delete_task, name='delete'),
]