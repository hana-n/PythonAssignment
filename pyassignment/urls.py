from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from . import settings
from django.contrib.staticfiles.urls import static
from foodreviews import views

urlpatterns = [
    path('foodreviews/', include('foodreviews.urls')),
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
