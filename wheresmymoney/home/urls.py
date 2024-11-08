from django.urls import path

from . import views

urlpatterns = [
    # path('home/', views.home),
    path('home/', views.HomeView.as_view(), name="home"),
    
    # path('authorized/', views.authorized)
    path('authorized/', views.AuthorizedView.as_view(), name="auth"),
    
    path('login/', views.LoginInterfaceView.as_view(), name="login"),
    path('loggedout/', views.LogoutConfirmView.as_view(),name='loggedout'),

    path('logout/', views.LogoutInterfaceView.as_view(),name='logout'),
    
]