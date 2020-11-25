from django.urls import path
from .views import home , updateTask , delete

urlpatterns = [
    path('',home, name="list"),
    path('update_task/<str:pk>/',updateTask, name="update_task"),
    path('delete/<str:pk>/',delete, name="delete")
]