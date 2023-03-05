from django.urls import path
from . import views

urlpatterns = [
    path('new_post/', views.new_post, name="new_post"),
    path('your_posts/', views.your_posts, name="your_posts"),    
    path('remove_book/<int:id>', views.remove_book, name='remove_book'),
    path('show_book/<int:id>', views.show_book, name="show_book"),
    ]