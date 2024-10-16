from django.urls import path
from . import views


urlpatterns = [        
    path('movies/', views.MovieCreateListView.as_view(), name='movie-create-list'),
    path('movies/<int:pk>/', views.MovieRetrieveUdpateDestroyView.as_view(), name='movie-detail-view'),
]
