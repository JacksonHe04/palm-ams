from django.db import models
from django.contrib.auth.hashers import make_password

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    auto_login_days = models.IntegerField(default=7)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._password_changed = False

    def set_password(self, raw_password):
        self.password = raw_password
        self._password_changed = True

    def save(self, *args, **kwargs):
        if self._state.adding or self._password_changed:
            self.password = make_password(self.password)
            self._password_changed = False
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'api_auth_user'