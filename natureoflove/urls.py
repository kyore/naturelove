from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from main_app import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('shop/', views.ProductListView.as_view(), name='shop'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('c/', include('main_app.urls')),
    path('blog/', include('blog.urls')),
]
