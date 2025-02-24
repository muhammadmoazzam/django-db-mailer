from django.urls import path, re_path
from dbmail.views import (
    send_by_dbmail, mail_read_tracker,
    SafariPushPackagesView, SafariSubscriptionView, SafariLogView,
    PushSubscriptionView
)

urlpatterns = [
    path('api/', send_by_dbmail, name='db-mail-api'),

    re_path(r'^mail_read_tracker/(?P<tracker_id>.*?)/$', mail_read_tracker, name='db-mail-tracker'),

    re_path(r'^safari/v(?P<version>\d)/pushPackages/(?P<site_pid>[.\w-]+)/?$', 
            SafariPushPackagesView.as_view()),

    re_path(r'^safari/v(?P<version>\d)/devices/(?P<device_token>[.\w-]+)/registrations/(?P<site_pid>[.\w-]+)/?$',
            SafariSubscriptionView.as_view()),

    re_path(r'^safari/v(?P<version>\d)/log/?$', SafariLogView.as_view()),

    re_path(r'^(?P<reg_type>web-push|mobile)/subscribe/$', PushSubscriptionView.as_view(), name='push-subscribe'),
    re_path(r'^(?P<reg_type>web-push|mobile)/unsubscribe/$', PushSubscriptionView.as_view(), name='push-unsubscribe'),
]
