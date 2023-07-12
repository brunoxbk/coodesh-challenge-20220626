from django.urls import path
from products import views

app_name = "products"

urlpatterns = [
    path('', views.ProductList.as_view(), name='list'),
    path('<int:code>/', views.ProductDetail.as_view(), name='detail'),
]
