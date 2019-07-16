from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from . import settings
from django.contrib.staticfiles.urls import static
from foodreviews import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(template_name='foodreviews/index.html'), name='home'),
    path('foodreviews/', include('foodreviews.urls')),
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
