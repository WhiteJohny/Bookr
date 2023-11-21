from django.urls import path
from reviews import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_details, name='book_detail')
]
