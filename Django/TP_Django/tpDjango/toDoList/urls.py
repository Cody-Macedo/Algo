from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update_task/<str:pk>', views.updateTask, name='update_task'),
    path('deleteTask/<str:pk>', views.deleteTask, name='delete_task'),
    path('doneTask/<str:pk>', views.doneTask, name='done_task'),
]
