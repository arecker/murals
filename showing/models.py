from django.db import models
from django.core.urlresolvers import reverse
from sorl.thumbnail import ImageField
from adminsortable.models import SortableMixin

from uuid import uuid4


class Gallery(SortableMixin, models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid4,
                          editable=False,
                          unique=True)

    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    order = models.PositiveIntegerField(default=0,
                                        editable=False,
                                        db_index=True)

    def get_absolute_url(self):
        return reverse('gallery-detail',
                       args=[str(self.slug)])

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['order']
        verbose_name_plural = 'Galleries'


class ItemQuerySet(models.QuerySet):
    def in_carousel(self):
        return self.filter(in_carousel=True)


class Item(models.Model):
    objects = ItemQuerySet.as_manager()

    id = models.UUIDField(primary_key=True,
                          default=uuid4,
                          editable=False,
                          unique=True)

    gallery = models.ForeignKey(Gallery,
                                null=True,
                                blank=True)
    image = ImageField(upload_to='uploads/')
    in_carousel = models.BooleanField(default=True, verbose_name='In home carousel')

    def __unicode__(self):
        return getattr(self, 'title', None) or str(self.pk)
