from django.core.cache import cache
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from .models import Expense


@receiver([post_save, post_delete], sender=Expense)
def invalidate_expense_caches(sender, instance, **kwargs):
    user_id = instance.user_id

    keys_to_delete = [f"category_list_user_{user_id}", f"expense_list_user_{user_id}"]

    cache.delete_many(keys_to_delete)
