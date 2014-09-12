from django.shortcuts import render_to_response
from managers import ImageManager, GalleryManager, get_navbar


class Data:
    pass


def get_home(request):
    data = Data()
    data.navbar = get_navbar()
    data.carousel = ImageManager.get_carousel_images()

    return render_to_response("home.html", {"data":data})


def get_gallery(request, slug):
    data = Data()
    data.navbar = get_navbar()
    data.images = ImageManager.get_images_by_gallery_slug(slug)
    data.gallery = GalleryManager.get_gallery_by_slug(slug)

    return render_to_response("gallery.html", {"data":data})


def get_contact(request):
    data = Data()
    data.navbar = get_navbar()
    return render_to_response("contact.html", {"data":data})