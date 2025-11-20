from django.urls import include, path

urlpatterns = [
    path("auth/", include("allauth.urls")),
    path("_allauth/", include("allauth.headless.urls")),
]
