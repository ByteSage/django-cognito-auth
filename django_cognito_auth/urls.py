from django_cognito_auth.settings import URL_PREFIX
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

urlpatterns = [
    url(settings.URL_PREFIX, include([
        url(r'^admin/', admin.site.urls),
        # Custom apps URLS
        url(r'^auth/', include('authentication.urls')),
    ])),
]
