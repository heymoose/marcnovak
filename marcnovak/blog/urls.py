from django.urls import path
from blog.views import (
    PostListView,
    PostDetailView,
)


urlpatterns = [
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('', PostListView.as_view(), name='post_list'),
]
