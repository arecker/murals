from markdown2 import markdown_path as MD
from BeautifulSoup import BeautifulSoup as HTML
from os.path import dirname, realpath, join


class Gallery:
    def __init__(self, Title, Description, Images):
        self.title = Title
        self.description = Description
        self.images = Images


raw = MD(realpath(join(dirname(__file__), 'galleries.md')))
galleries = []
for p in HTML(raw).findAll('p'):
    title, description = p.string.split(': ')
    images = []
    for li in p.findNext('ul').findChildren():
        images.append(li.string)
    galleries.append(Gallery(title, description, images))
    
