from django.urls import path
from . import views

app_name = 'wb_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('registration/', views.register, name='registration'),
    path('account/', views.account_view, name='account'),
    path('products/', views.product_view, name='product-view'),
    path('products/<int:pk>', views.product_detail, name='transactions_view')
]