from django.urls import path
from . import views

urlpatterns = [
    path('reviews/', views.ReviewCreateListView.as_view(), name='review-creat-list'),
    path('reviews/<int:pk>/', views.ReviewretrieveUpdateDestroyView.as_view(), name='review-detail-view')
]
