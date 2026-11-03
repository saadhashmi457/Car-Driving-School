from django.urls import path
from Myapp import views

urlpatterns = [
    path('', views.home_view, name='homepage'),
    path('/services', views.service_view, name='servicepage'),
    path('/contacts', views.contacts_view, name='contactpage'),
    path('/signup', views. signup_view, name='signuppage'),
    path('/login', views.login_view, name='loginpage'),
    
    # path('about/', views.about_view, name='about'),
    # path('reservations/', views.reservations_view, name='reservations'),
    # path('signup/', views.signup_view, name='signup'),
    # path('login/', views.login_view, name='login'),
    # path('logout/', views.logout_view, name='logout'),
    # path('ireservation/', views.ireservation_view, name='ireservation'),

   
]