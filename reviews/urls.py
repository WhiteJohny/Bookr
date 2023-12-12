from django.urls import path
from reviews import views

urlpatterns = [
    path('books/', views.books_list, name='books_list'),
    path('book/<int:pk>/', views.book_details, name='book_details')
]
