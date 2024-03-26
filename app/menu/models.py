from typing import Optional
from django.db import models
from django.urls import reverse


# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=20, unique=True, null=False)
    named_url = models.CharField(
        max_length=255,
        verbose_name="Named URL",
        blank=True,
        help_text="Named url from your urls.py file",
    )

    class Meta:
        ordering = ["id"]

    def __str__(self) -> str:
        return self.name

    def get_url(self):
        if self.named_url:
            url = reverse(self.named_url)
        else:
            url = "{}/".format(self.name)
        return url

    def check_prefetch(self):
        try:
            self._prefetched_objects_cache
            return True
        except (AttributeError, KeyError):
            return False


class MenuItem(models.Model):
    name = models.CharField(max_length=20, null=False, blank=True, unique=True)
    menu = models.ForeignKey(
        Menu,
        related_name="items",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="items",
    )
    link = models.URLField(max_length=255, blank=True)

    data = models.CharField(max_length=200, blank=True)

    named_url = models.CharField(
        max_length=255,
        blank=True,
        help_text="Named url from your urls.py file",
    )

    def __str__(self) -> str:
        return self.name

    def get_url(self):
        if self.named_url:
            url = reverse(self.named_url)
        else:
            url = "{}/".format(self.name)

        return url

    def check_prefetch(self):
        try:
            self._prefetched_objects_cache
            return True
        except (AttributeError, KeyError):
            return False
