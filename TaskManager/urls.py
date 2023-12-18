from django.urls import path, include
from django.views.generic import TemplateView
from TaskManager import views
from .views import CreateTask, TaskList, TaskDetail, DeleteTask

urlpatterns = [
    path('', views.inicio, name="Dashboard" ),
    path('mylist/', TaskList.as_view(), name="TaskList"),
    path('create-task', CreateTask.as_view(), name="CreateTask"),
    path('delete-task/<pk>', DeleteTask.as_view(), name="DeleteTask"),
    path('detail-tasks/<pk>', TaskDetail.as_view(), name="DetailTasks"),
    path('create_subtask/<int:task_id>/',views.create_subtask, name='create_subtask'),
    path('update_subtask_state/<int:subtask_id>/<str:subtask_state>/', views.update_subtask_state, name='update_subtask_state'),
    ]