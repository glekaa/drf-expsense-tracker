from allauth.headless.contrib.rest_framework.authentication import (
    JWTTokenAuthentication,
)
from django.core.cache import cache
from django.db.models import DecimalField, Q, Sum
from django.db.models.functions import Coalesce
from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response

from .models import Category, Expense
from .serializers import CategorySerializer, ExpenseSerializer


class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    authentication_classes = [JWTTokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Category.objects.annotate(
            total_spent=Coalesce(
                Sum("expenses__amount", filter=Q(expenses__user=self.request.user)),
                0,
                output_field=DecimalField(),
            )
        )

    def list(self, request, *args, **kwargs):
        user_id = request.user.id
        cache_key = f"category_list_user_{user_id}"

        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data)

        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data

        cache.set(cache_key, data, timeout=60 * 15)

        return Response(data)


class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    authentication_classes = [JWTTokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Expense.objects.filter(user_id=self.request.user.id)

    def list(self, request, *args, **kwargs):
        user_id = request.user.id
        cache_key = f"expense_list_user_{user_id}"

        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data)

        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data

        cache.set(cache_key, data, timeout=60 * 15)

        return Response(data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
