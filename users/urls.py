from django.urls import path
from users import views

urlpatterns = [
    path('register/customer/', views.register_customer, name='register_customer'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.user_logout, name='logout'),
    
]
