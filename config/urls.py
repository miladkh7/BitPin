
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

api_version ="1"
urlpatterns = [
    path("admin/", admin.site.urls),
    path(f'api/v{api_version}/', include('config.api_v1')),
]
if settings.DEBUG:
    
    urlpatterns_develop = [
        path("__debug__/", include("debug_toolbar.urls")),

        path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
        # Optional UI:
        path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
        path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    ]
    urlpatterns += urlpatterns_develop

