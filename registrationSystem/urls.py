
from django.contrib import admin
from django.urls import path, include
from django.conf import settings  ## to view uploaded files in local environment
from django.conf.urls.static import static  ## to view uploaded files in local environment

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

