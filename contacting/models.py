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
                                           editable=True)
    email = models.EmailField()
    subject = models.CharField(max_length=120)
    message = models.TextField()

    def log_ip(self, request):
        self.address = get_real_ip(request)

    def __unicode__(self):
        return '{0} ({1})'.format(self.subject, self.email)

    class Meta:
        ordering = ['-timestamp']
