from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns

from .provider import DaumProvider


urlpatterns = default_urlpatterns(DaumProvider)
