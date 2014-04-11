from markdown2 import markdown_path as MD
from BeautifulSoup import BeautifulSoup as HTML
from slugify import slugify as Slugify
from os.path import dirname, realpath, join


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


def GetGalleries():
    raw = MD(realpath(join(dirname(__file__), 'galleries.md')))
    galleries = []
    for p in HTML(raw).findAll('p'):
        title, description = p.string.split(': ')
        images = []
        for li in p.findNext('ul').findChildren():
            images.append(li.string)
        galleries.append(Gallery(Title=title, Description=description, Slug=Slugify(title), Images=images))
    return galleries


def GetContactMe():
    raw = MD(realpath(join(dirname(__file__), 'contact.md')))

def GetHomePage():
    raw = HTML(MD(realpath(join(dirname(__file__), 'home.md'))))
    junk, bio = raw.find('p').string.split('Bio: ')
    slideshow = []
    for li in raw.findAll('li'):
        slideshow.append(li.string)
    return HomePage(Bio=bio, Slideshow=slideshow)