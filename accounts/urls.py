from django.urls import path 
from . import views 

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    
    # path('activate/<uidb64>/<token>/', views.activate, name="activate"),
    path('activate/', views.activate, name="activate"),
    path('', views.dashboard, name="dashboard"),
    path('Forgot_password', views.Forgot_password, name="Forgot_password"),
]
