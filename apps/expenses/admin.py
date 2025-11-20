from django.contrib import admin
from .models import Category, Expense

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("name", "amount", "category", "user", "created_at")
    list_filter = ("category", "created_at", "user")
    search_fields = ("name", "user__email")
