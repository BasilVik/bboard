from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser


class AdvUser(AbstractUser):
    is_activated = models.BooleanField(
        default=True,
        db_index=True,
        verbose_name='Прошел активацию?'
    )

    send_messages = models.BigAutoField(
        default=True,
        verbose_name='Присылать оповещения о новых комментариях?'
    )

    class Meta(AbstractUser.Meta):
        pass
