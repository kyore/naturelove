from django.urls import path

from blog.views import PostListView, PostDetailView

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='list'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
]
