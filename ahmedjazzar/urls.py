
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from ahmedjazzarcom import views

urlpatterns = [
    url(r'^super/', include(admin.site.urls)),
    url(r'^$', views.Home.as_view(), name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)