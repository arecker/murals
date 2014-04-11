from django.shortcuts import render_to_response
from django.conf.urls import patterns
from markdown2 import markdown_path as MD
from BeautifulSoup import BeautifulSoup as HTML
from slugify import slugify as Slugify
from os.path import dirname, realpath, join, splitext, abspath


## Globals
def MAP(fileName):
    filepath, extension = splitext(__file__)
    CONTENT = abspath(join(filepath, '..', 'Content'))
    return join(CONTENT, fileName)


### Models
class Gallery:
    def __init__(self, Title, Description, Slug, Images):
        self.title = Title
        self.description = Description
        self.slug = Slug
        self.images = Images


class HomePage:
    def __init__(self, Bio, Slideshow):
        self.bio = Bio
        self.slideshow = Slideshow


### Controllers
def GetHome(request):
    return render_to_response('home.html', {
        'HomePage': ReadHomePage(),
    })


def GetGallery(request, slug):
    gallery_list = filter(lambda s: s.slug == slug, ReadGalleries())

    if gallery_list[0] is None:
        pass #404
    else:
        gallery = gallery_list[0]

    return render_to_response('gallery.html', {
        'Gallery': ReadContactMe()
    })


def GetContactMe(request):
    return render_to_response('contact.html', {
        'Text': ReadContactMe()
    })


### Helpers
def ReadHomePage():
    raw = HTML(MD(MAP('home.md')))
    junk, bio = raw.find('p').string.split('Bio: ')
    slideshow = []
    for li in raw.findAll('li'):
        slideshow.append(li.string)
    return HomePage(Bio=bio, Slideshow=slideshow)


def ReadGalleries():
    raw = MD(MAP('galleries.md'))
    galleries = []
    for p in HTML(raw).findAll('p'):
        title, description = p.string.split(': ')
        images = []
        for li in p.findNext('ul').findChildren():
            images.append(li.string)
        galleries.append(Gallery(Title=title, Description=description, Slug=Slugify(title), Images=images))
    return galleries


def ReadContactMe():
    return MD(MAP('contact.md'))


### Routes
urlpatterns = patterns('',
    (r'^$', GetHome),
    (r'^contact/', GetContactMe),
    (r'^(?P<slug>[^/]+)', GetGallery),
)