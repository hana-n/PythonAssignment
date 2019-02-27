from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('foodreviews/', include('foodreviews.urls')),
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
]