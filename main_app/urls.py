from django.urls import path
from .views import *

app_name = 'category'

urlpatterns = [
    path('<slug:slug>/', CategoryDetailView.as_view(), name='detail'),
    path('<slug:parent>/<slug:slug>/', SubCategoryDetailView.as_view(), name='sub-detail'),
]
