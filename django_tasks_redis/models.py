"""
Pseudo-model backing the Django Admin integration.

Redis tasks are stored in Redis, not in the database. This model exists so the
admin can register a ModelAdmin against them, and so Django creates the
permissions that guard it. It is unmanaged and has no table.
"""

from django.db import models
from django.utils.translation import gettext_lazy as _


class RedisTask(models.Model):
    """
    Pseudo-model for Redis tasks in Django Admin.

    This model is not actually stored in the database.
    It's used to provide a Django Admin interface for Redis tasks.
    """

    task_id = models.CharField(max_length=36, primary_key=True)

    class Meta:
        managed = False
        app_label = "django_tasks_redis"
        # There is no table, so tasks can never be added or edited from the
        # admin: it reads them, runs them and deletes them.
        default_permissions = ("view", "delete")
        permissions = [("run_redistask", _("Can run Redis task"))]
        verbose_name = _("Redis Task")
        verbose_name_plural = _("Redis Tasks")
