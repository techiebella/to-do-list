from django.contrib import admin
from django.urls import path
from tasks import views as task_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', task_views.task_list, name='task_list'),

    path('create/', task_views.task_create, name='task_create'),
    path('update/<int:pk>/', task_views.task_update, name='task_update'),
    path('delete/<int:pk>/', task_views.task_delete, name='task_delete'),

    path('complete/<int:pk>/', task_views.task_complete, name='task_complete'),

    path('login/', task_views.login_view, name='login'),
    path('register/', task_views.register_view, name='register'),

    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]