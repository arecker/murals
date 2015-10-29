from django.views.generic import DetailView, TemplateView

from models import Gallery, Item


class Index(TemplateView):
    template_name = 'showing/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Index, self).get_context_data(*args, **kwargs)
        context['carousel'] = Item.objects.in_carousel()
        return context


class GalleryDetail(DetailView):
    model = Gallery
