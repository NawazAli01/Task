from django.urls import path, include
from . import views

app_name = 'task_app'

urlpatterns = [
    path('task_app/',views.ListCreateAPI.as_view(),name='task_app'),
]
