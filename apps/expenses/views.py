from allauth.headless.contrib.rest_framework.authentication import (
    JWTTokenAuthentication,
)
from rest_framework import generics, permissions, viewsets

from .models import Category, Expense
from .serializers import CategorySerializer, ExpenseSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    authentication_classes = [JWTTokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Expense.objects.filter(user_id=self.request.user.id)
