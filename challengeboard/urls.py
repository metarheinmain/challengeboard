from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('board.urls', namespace='board')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
