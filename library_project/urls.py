from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Book list view",
        default_version='v1',
        description='Library demo project',
        terms_of_service='demo.com',
        contact=openapi.Contact(email='ikromjon01021995@gmail.com'),
        license=openapi.License(name='demo license'),
    ),
    public=True,
    permission_classes=[permissions.AllowAny,],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('books.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/dj_rest_auth/', include('dj_rest_auth.urls',)),




    # swagger
    path('swagger', schema_view.with_ui(
        'swagger', cache_timeout=0), name='swagger-swagger-ui'),
    path('redoc/', schema_view.with_ui(
        'redoc', cache_timeout=0), name='swagger-redoc')
]
