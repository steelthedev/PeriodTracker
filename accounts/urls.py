from django.urls import path
from . import views


app_name='accounts'
urlpatterns=[
  
  path('signup',views.SignupView,name="signup"),
  path('signin',views.LoginView,name='signin'),
  path('logout',views.LogoutView,name='logout')
  ]