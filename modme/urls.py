from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('admin/', admin.site.urls),
    path('api/accounts', include('accounts.urls')),
    path('api/courses', include('courses.urls')),

    path('auth/djoser/', include('djoser.urls')),
    path('auth/', include('rest_framework.urls')),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
