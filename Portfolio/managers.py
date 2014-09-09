from models import *

class Data:
    pass


class ImageManager:
    @staticmethod
    def get_carousel_images():
        return Image.objects.filter(carousel=True)


    @staticmethod
    def get_images_by_gallery_slug(slug):
        try:
            gallery = Gallery.objects.get(slug = slug)
        except Gallery.DoesNotExist:
            return None

        try:
            return Image.objects.filter(gallery=gallery)
        except: # general error
            return None


class GalleryManager:
    @staticmethod
    def get_galleries():
        return Gallery.objects.all().order_by('title')


def get_navbar():
    data = Data()
    data.galleries = GalleryManager.get_galleries()
    return data