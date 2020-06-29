from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name="home"),
    path('', views.home,name="home"),
    path('login/',views.login,name="login"),
    path('register/',views.register,name="register"),
    path('v/', views.v,name="v"),
    path('scrap/', views.Scrap,name="scrap"),
    path('ph/', views.ph,name="ph"),
    path('visual/', views.visual,name="visual"),
    path('alert/', views.alert,name="alert"),
    path('logout/',views.logout,name="logout"),
    path('chart/', views.Chart.as_view()), 
    path('api/', views.ChartData.as_view()),




    
]