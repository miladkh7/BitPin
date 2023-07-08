# Standard
import uuid

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from django.conf import settings


class User(AbstractUser):
    """
    Default custom user model for BitPin.
    """

    #: for security reason use uuid4
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(_("First Name"), max_length=55, null=True, blank=True)
    last_name = models.CharField(_("First Name"), max_length=55, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
