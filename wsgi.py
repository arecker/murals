import os, sys
try:
    sys.path.append('/PATH/TO/PROJECT/FILES')
    os.environ['DJANGO_SETTINGS_MODULE'] = 'Blog.settings'
    activate_this = "/PATH/TO/VIRTUALENV/bin/activate_this.py"
    execfile(activate_this, dict(__file__=activate_this))
except:
    pass
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()