from django.shortcuts import render_to_response
from managers import ImageManager, get_navbar


class Data:
    pass


def get_home(request):
    data = Data()
    data.navbar = get_navbar()
    data.carousel = ImageManager.get_carousel_images()

    return render_to_response("home.html", {"data":data})