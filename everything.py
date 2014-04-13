from django.shortcuts import render_to_response, HttpResponseRedirect
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
    def __init__(self, Title, Description=None, Images=None):
        self.title = Title
        self.description = Description
        self.slug = Slugify(Title)
        self.images = Images


class HomePage:
    def __init__(self, Bio, Slideshow):
        self.bio = Bio
        self.slideshow = Slideshow


### Controllers
def GetHome(request):
    return render_to_response('base.html', {
        'Galleries': ReadGalleries(),
        'HomePage': ReadHomePage(),
    })


def GetGallery(request, slug):
    gallery_list = filter(lambda s: s.slug == slug, ReadGalleries())

    try:
        focus_gallery = gallery_list[0]
    except:
        return HttpResponseRedirect('/')

    return render_to_response('gallery.html', {
        'Focus_Gallery': focus_gallery,
        'Galleries': ReadGalleries(),
    })


def GetContactMe(request):
    return render_to_response('base.html', {
        'Galleries': ReadGalleries(),
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
        galleries.append(Gallery(Title=title, Description=description, Images=images))
    return galleries


def ReadContactMe():
    return MD(MAP('contact.md'))


def ReadGalleryLinks():
    raw = MD(MAP('galleries.md'))
    galleries = []
    for p in HTML(raw).findAll('p'):
        title, description = p.string.split(': ')
        galleries.append(Gallery(title))
    return galleries


### Routes
urlpatterns = patterns('',
    (r'^$', GetHome),
    (r'^contact$', GetContactMe),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve'),
    (r'^(?P<slug>[^/]+)', GetGallery),
)