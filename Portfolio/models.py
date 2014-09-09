from django.db import models
from MJAI import settings
from django.template.defaultfilters import slugify
from PIL import Image as PILImage
from cStringIO import StringIO
from django.core.files.uploadedfile import SimpleUploadedFile
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
    thumbnail = models.ImageField(upload_to=settings.UPLOADS, blank=True, null=True, editable=False)
    gallery = models.ForeignKey(Gallery, blank=True, null=True, on_delete=models.SET_NULL)
    order = models.IntegerField(blank = True, null = True)
    carousel = models.BooleanField(default=False, verbose_name="Include in Carousel")


    class Meta:
        ordering = ('order',)


    def save(self, *args, **kwargs):
        self.create_thumbnail()
        super(Image, self).save(*args, **kwargs)


    def filename(self):
        return os.path.basename(self.file.name)


    def thumb_filename(self):
        return os.path.basename(self.thumbnail.file.name)


    def __unicode__(self):
        return self.name


    def image_thumb(self):
        return '<img src="/uploads/%s" width="100" height="100" />' % (self.thumb_filename())

    image_thumb.allow_tags = True

    def create_thumbnail(self):
        if not self.file:
            return

        THUMBNAIL_SIZE = (200,200)
        DJANGO_TYPE = self.file.file.content_type

        if DJANGO_TYPE == 'image/jpeg':
            PIL_TYPE = 'jpeg'
            FILE_EXTENSION = 'jpg'
        elif DJANGO_TYPE == 'image/png':
            PIL_TYPE = 'png'
            FILE_EXTENSION = 'png'

        image = PILImage.open(StringIO(self.file.read()))
        image.thumbnail(THUMBNAIL_SIZE, PILImage.ANTIALIAS)

        # Save the thumbnail
        temp_handle = StringIO()
        image.save(temp_handle, PIL_TYPE)
        temp_handle.seek(0)

        suf = SimpleUploadedFile(os.path.split(self.file.name)[-1], temp_handle.read(), content_type=DJANGO_TYPE)
        self.thumbnail.save(
            '%s_thumbnail.%s'%(os.path.splitext(suf.name)[0],FILE_EXTENSION), suf, save=False)

 