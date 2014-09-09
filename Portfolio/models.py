from django.db import models
from MJAI import settings
from django.template.defaultfilters import slugify
import os


class Gallery(models.Model):
    title = models.CharField(max_length=50, verbose_name="Title")
    description = models.TextField(blank=True, verbose_name="Description")
    slug = models.SlugField(editable=False)

    class Meta:
        verbose_name_plural = 'Galleries'


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Gallery, self).save(*args, **kwargs)


    def __unicode__(self):
        return self.title


class Image(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name")
    caption = models.TextField(blank=True, verbose_name="Caption")
    file = models.ImageField(upload_to=settings.UPLOADS)
    gallery = models.ForeignKey(Gallery, blank=True, null=True, on_delete=models.SET_NULL)
    order = models.IntegerField(blank = True, null = True)
    carousel = models.BooleanField(default=False, verbose_name="Include in Carousel")


    class Meta:
        ordering = ('order',)


    def filename(self):
        return os.path.basename(self.file.name)


    def __unicode__(self):
        return self.name


    def image_thumb(self):
        return '<img src="/uploads/%s" width="100" height="100" />' % (self.filename())

    image_thumb.allow_tags = True