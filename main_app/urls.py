from django.urls import path
from .views import *

app_name = 'category'

urlpatterns = [
    path('email/<int:product_id>/', send_email_view, name='send-email'),
    path('<slug:slug>/', CategoryDetailView.as_view(), name='detail'),
    path('<slug:parent>/<slug:slug>/', SubCategoryDetailView.as_view(), name='sub-detail'),
]
