from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('products.urls')),
]

# Serve media files and use staticfiles finders for static files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Use staticfiles_urlpatterns so app/static and contrib static files (admin) are served
    urlpatterns += staticfiles_urlpatterns()
