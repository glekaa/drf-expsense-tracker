from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CategoryListView, ExpenseViewSet

router = DefaultRouter()
router.register("expenses", ExpenseViewSet, basename="expense")

urlpatterns = [path("categories/", CategoryListView.as_view())] + router.urls
