from django.urls import path
from . import views

app_name = 'wb_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('registration/', views.register, name='registration')
]