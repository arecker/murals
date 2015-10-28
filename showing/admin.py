from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from adminsortable.admin import SortableAdmin

from models import Item, Gallery


class ItemAdmin(AdminImageMixin, admin.StackedInline):
    model = Item
    extra = 1


class GalleryAdmin(SortableAdmin):
    inlines = [ItemAdmin]
    prepopulated_fields = {'slug': ['title']}


admin.site.register(Gallery, GalleryAdmin)
