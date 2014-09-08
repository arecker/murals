from os.path import join, splitext, abspath
from flask import Flask, Response
app = Flask(__name__)


### Global Variables
filepath, extension = splitext(__file__)
PAGES = abspath(join(filepath, '..', 'content/pages'))
POSTS = abspath(join(filepath, '..', 'content/posts'))
CACHE = abspath(join(filepath, '..', 'cache'))
STATIC = abspath(join(filepath, '..', 'static'))


### Controllers
@app.route("/")
def GetHome():
    home_page = open(join(CACHE, 'pages/home.html'), 'r').read()
    return home_page


@app.route("/archives/")
def GetArchives():
    archives_page = open(join(CACHE, 'pages/archives.html'), 'r').read()
    return archives_page


@app.route("/contact/")
def GetContactPage():
    contact_page = open(join(CACHE, 'pages/contact.html'), 'r').read()
    return contact_page


@app.route("/<slug>/")
def GetGallery(slug):
    try:
        post = open(join(CACHE, 'galleries/' + slug + '.html'), 'r').read()
        return post
    except:
        missing_page = open(join(CACHE, 'pages/404.html'), 'r').read()
        return missing_page


@app.route("/blog/<slug>/")
def GetPost(slug):
    try:
        post = open(join(CACHE, 'posts/' + slug + '.html'), 'r').read()
        return post
    except:
        missing_page = open(join(CACHE, 'pages/404.html'), 'r').read()
        return missing_page


### Init App
if __name__ == "__main__":
    app.debug = True
    app.run()
