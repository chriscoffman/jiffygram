from django.urls import path 

from .views import (
    PostListView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView,
    PostCreateView,
    LikeView,
)
urlpatterns = [ 
    path('<int:pk>/', PostDetailView.as_view(),
    name = 'post_detail'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('new/', PostCreateView.as_view(), name='post_new'),
    path('', PostListView.as_view(), name='post_list'),
    path('like/<int:pk>', LikeView, name='like_post'),
]