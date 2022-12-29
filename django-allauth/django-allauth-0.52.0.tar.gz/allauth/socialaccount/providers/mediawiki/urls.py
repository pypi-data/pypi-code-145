from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns

from .provider import MediaWikiProvider


urlpatterns = default_urlpatterns(MediaWikiProvider)
