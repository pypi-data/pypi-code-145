from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns

from .provider import WeiboProvider


urlpatterns = default_urlpatterns(WeiboProvider)
