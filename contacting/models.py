from django.db import models
from ipware.ip import get_real_ip

from uuid import uuid4


class Message(models.Model):
    id = models.UUIDField(primary_key=True,
                          editable=False,
                          unique=True,
                          default=uuid4)

    timestamp = models.DateTimeField(editable=False,
                                     auto_now_add=True)
    address = models.GenericIPAddressField(null=True,
                                           blank=True)
    email = models.EmailField()
    message = models.TextField()

    def log_ip(self, request):
        self.address = get_real_ip(request)

    class Meta:
        ordering = ['-timestamp']
