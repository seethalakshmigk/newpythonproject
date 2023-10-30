from django.urls import path
from . import views
from .models import Task

app_name = "todoapp"

urlpatterns = [
    path('', views.add, name="add"),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),

]


