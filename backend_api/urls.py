from django.conf import settings
from django.urls import include, path
from django.views.generic import RedirectView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import (
    TokenBlacklistView,
    TokenObtainPairView,
    TokenRefreshView,
)

api_urlpatterns = [
    path(
        "auth/",
        include(
            [
                path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
                path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
                path("logout/", TokenBlacklistView.as_view(), name="token_blacklist"),
            ]
        ),
    ),
    path("ibook/", include("ibook.urls")),
]

urlpatterns = [
    path("api/", include(api_urlpatterns)),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
        path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
        path(
            "swagger-ui/",
            SpectacularSwaggerView.as_view(url_name="schema"),
            name="swagger-ui",
        ),
        path("", RedirectView.as_view(url="swagger-ui/")),
        path("api-auth/", include("rest_framework.urls")),
    ] + urlpatterns
