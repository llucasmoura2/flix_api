from django.urls import path
from . import views

urlpatterns = [

    path('actors/', views.ActorsListCreatView.as_view(), name='actor-create-list'),
    path('actors/<int:pk>/', views.ActorsRetrieveUpdateDestroyView.as_view(), name='actor-detail-view'),
]
