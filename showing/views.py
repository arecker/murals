from django.views.generic import DetailView, TemplateView

from models import Gallery


class Index(TemplateView):
    template_name = 'showing/index.html'


class GalleryDetail(DetailView):
    model = Gallery
