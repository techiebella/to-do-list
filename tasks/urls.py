from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    # 📊 MAIN TASK DASHBOARD
    path('', views.task_list, name='task_list'),

    # ➕ CRUD OPERATIONS
    path('create/', views.task_create, name='task_create'),
    path('update/<int:pk>/', views.task_update, name='task_update'),
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),

    # ✔ COMPLETE / TOGGLE
    path('complete/<int:pk>/', views.task_complete, name='task_complete'),

    # 🔐 AUTH PAGES
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),

    # 🚪 LOGOUT (BEST PRACTICE VERSION)
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]