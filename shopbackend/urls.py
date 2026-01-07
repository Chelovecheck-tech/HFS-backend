from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('products.urls')),
]

# Serve media files in production (Railway) and development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Use staticfiles_urlpatterns for static files
urlpatterns += staticfiles_urlpatterns()
