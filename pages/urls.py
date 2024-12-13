from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('learn/', views.learn, name='learn'),
    path('create/', views.create, name='create'),
    path('stats/', views.stats, name='stats'),
    path('about/', views.about, name='about'),
    path('account/profile/', views.profile, name='profile'),
    path('account/settings/', views.settings, name='settings'),
    path('account/payments/', views.payments, name='payments'),
]