from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),  # login default page
    path('home/', views.home, name='home'),
    path("accounts/",include("allauth.urls"))

]
