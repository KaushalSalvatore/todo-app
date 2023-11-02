from django.urls import path
from .views import (TaskList,
                    TaskDetails,
                    TaskCreate,
                    TaskUpdate,
                    TaskDelete,
                    CustomeLoginView,
                    RegisterPage)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/',RegisterPage.as_view(),name='register'),
    path('login/',CustomeLoginView.as_view(),name='login'),
    path('logout',LogoutView.as_view(next_page='login'),name='logout'),
    path('',TaskList.as_view(),name='tasks'),
    path('task/<int:pk>/', TaskDetails.as_view(),name='task'),
    path('create-task/',TaskCreate.as_view(),name='task-create'),
    path('task-update/<int:pk>/',TaskUpdate.as_view(),name='task-update'),
    path('task-delete/<int:pk>/',TaskDelete.as_view(),name='task-delete'),
]