from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from admin_panel.views import index

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('api/v1/', include('tests.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
