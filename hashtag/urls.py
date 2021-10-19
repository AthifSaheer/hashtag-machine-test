from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('api/v1/admin/', include('admin_panel.urls')),
    path('api/v1/', include('rest_framework.urls'))
]
