from markdown2 import markdown_path as MD
from BeautifulSoup import BeautifulSoup as HTML
from slugify import slugify as Slugify
from jinja2 import Environment, FileSystemLoader
from os.path import dirname, realpath, join, splitext, abspath

## Globals
filepath, extension = splitext(__file__)
CONTENT = abspath(join(filepath, '..', 'content'))
CACHE = abspath(join(filepath, '..', 'cache'))
ENV = Environment(loader=FileSystemLoader('templates'))


## Pages
class HomePage:
    def __init__(self):
        # Read in Content
        raw = HTML(MD(join(CONTENT, 'pages/home.md')))
        junk, bio = raw.find('p').string.split('Bio: ')
        slideshow = []
        for li in raw.findAll('li'):
            slideshow.append(li.string)

        # Set Properties
        self.bio = bio
        self.slideshow = slideshow


class Gallery:
    def __init__(self, title, slug, images, description):
        self.title = title
        self.description = description
        self.slug = slug
        self.images = images


class GalleryList:
    def __init__(self):
        self.galleries = []
        # Read in Galleries
        raw = MD(join(CONTENT, 'pages/galleries.md'))
        for p in HTML(raw).findAll('p'):
            title, description = p.string.split(': ')
            images = []
            for li in p.findNext('ul').findChildren():
                images.append(li.string)
            self.galleries.append(Gallery(title=title, slug=Slugify(title), images=images, description=description))


    def GetGalleries(self):
        # Returns a list of galleries for the dropdown in navbar
        return self.galleries



class CacheWriter:
    def __init__(self):
        self.gallery_list = GalleryList().GetGalleries()

    def WriteHome(self):
        template = ENV.get_template('home.html')
        with open(join(CACHE, 'pages', 'home.html'), 'wb') as file:
            file.write(template.render(HomePage = HomePage(), Galleries = self.gallery_list))


    def WriteGalleries(self):
        template = ENV.get_template('gallery.html')
        for gallery in self.gallery_list:
            with open(join(CACHE, 'galleries', gallery.slug + '.html'), 'wb') as file:
                file.write(template.render(Focus_Gallery = gallery, Galleries = self.gallery_list))


    def WriteContact(self):
        template = ENV.get_template('contact.html')
        raw = MD(join(CONTENT, 'pages/contact.md'))
        with open(join(CACHE, 'pages/contact.html'), 'wb') as file:
            file.write(template.render(Galleries = self.gallery_list, Text = raw))


# Call Methods and Log to console
cw = CacheWriter()
cw.WriteHome()
cw.WriteGalleries()
cw.WriteContact()