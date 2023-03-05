from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_books, name="search_books"),
    path('purchase_order/<int:id>', views.purchase_order, name="purchase_order")
]   