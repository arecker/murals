from django.shortcuts import render_to_response, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.views.generic import TemplateView

from forms import MessageForm


class Thanks(TemplateView):
    template_name = 'contacting/thanks.html'


def message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save(request)
            return HttpResponseRedirect(reverse('contact-thanks'))
    else:
        form = MessageForm()

    return render_to_response('contacting/contact.html',
                              RequestContext(request, {'form': form}))
