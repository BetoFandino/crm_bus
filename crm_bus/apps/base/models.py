from django.db import models

from simple_history.models import HistoricalRecords


class BaseModel(models.Model):
    """model base to be inherited for other models with this params"""
    id = models.AutoField(primary_key=True)
    state = models.BooleanField(default=True)
    created_date = models.DateField(auto_now=False, auto_now_add=True)
    modified_date = models.DateField(auto_now=True, auto_now_add=False)
    deleted_date = models.DateField(auto_now=True, auto_now_add=False)
    historical = HistoricalRecords(user_model="users.User", inherit=True)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """Meta definition for BaseModel."""
        abstract = True
        verbose_name = 'Model Base'
        verbose_name_plural = 'Models Base'
