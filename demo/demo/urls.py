import os
import sys
from django.urls import path, re_path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import demo.views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('rosetta/', include('rosetta.urls')),  # Uncomment if needed
    path('dbmail/', include('dbmail.urls')),
]

if 'test' not in sys.argv:
    urlpatterns += [
        path('grappelli/', include('grappelli.urls')),
        path('browser_notification/', demo.views.browser_notification),
        path('web-push/', demo.views.web_push_notification),
        path('ckeditor/', include('ckeditor_uploader.urls')),
    ]

# For security reasons, serve static & media files in DEBUG mode only
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
