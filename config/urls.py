from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("auth/", include("allauth.headless.urls")),
    path("", include("apps.expenses.urls")),
]
