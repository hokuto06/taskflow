from django.urls import path, include
from .views import user_login
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', user_login, name='user_login'),
]
