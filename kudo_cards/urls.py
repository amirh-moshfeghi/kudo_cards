from django.contrib import admin
from django.urls import include, path
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Kudo API Docs')
# urls
urlpatterns = [
    path('api/v1/kudos/', include('api.urls')),
    path('', schema_view, name='docs'),
    path('api/v1/auth/', include('authentication.urls')),
    path('admin/', admin.site.urls),
]
