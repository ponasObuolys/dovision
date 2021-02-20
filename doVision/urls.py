from django.contrib import admin
from django.urls import path, include

import debug_toolbar

from doVision import views


urlpatterns = [
    path('', views.listas, name='TodoList'),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
    path('delete/<str:pk>/', views.deleteTask, name="delete"),
    path('prior/<str:pk>/', views.prioritize, name='prior'),
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('completed/<str:pk>/', views.completed_task, name='completed'),
]
