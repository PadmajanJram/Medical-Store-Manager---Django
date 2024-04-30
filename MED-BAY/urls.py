from django.contrib import admin
from django.urls import path, include
from medicals import views
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', views.medicals,name='home'),
    path('products/',include('products.urls')),
    path('signup/',views.signup_page,name='signup'),
    path('login/',views.login_page,name='login'),
    path('logout/', views.logout_view,name='logout'),
    path('productsapi/',include('productsapi.urls'))
]