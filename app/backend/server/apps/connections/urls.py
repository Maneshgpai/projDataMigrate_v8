from django.urls import include, re_path
from apps.connections import views

connections_urlpatterns = [
    re_path(r'^api/v1/', include('djoser.urls')),
    re_path(r'^api/v1/', include('djoser.urls.authtoken')),
    re_path(r'^source$',views.sourceConnectionApi),
    re_path(r'^source/([0-9]+)$',views.sourceConnectionApi),
    re_path(r'^destination$',views.destConnectionApi),
    re_path(r'^destination/([0-9]+)$',views.destConnectionApi)
]
