from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models


class News(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    title = models.CharField(max_length=120)
    content = models.TextField()
    header_image = models.ImageField(null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("news:detail", kwargs={"id": self.id})

    class Meta:
        ordering = ["-timestamp", "-updated"]
