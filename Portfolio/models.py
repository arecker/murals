from django.db import models
from MJAI import settings
import os


class Gallery(models.Model):
    title = models.CharField(max_length=50, verbose_name="Title")
    description = models.TextField(blank=True, verbose_name="Description")


    class Meta:
        verbose_name_plural = 'Galleries'


    def __unicode__(self):
        return self.title


class Image(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name")
    caption = models.TextField(blank=True, verbose_name="Caption")
    file = models.ImageField(upload_to=settings.UPLOADS)
    gallery = models.ForeignKey(Gallery, blank=True, null=True, on_delete=models.SET_NULL)


    def filename(self):
        return os.path.basename(self.file.name)


    def __unicode__(self):
        return self.name


    def image_thumb(self):
        return '<img src="/uploads/%s" width="100" height="100" />' % (self.filename())

    image_thumb.allow_tags = True