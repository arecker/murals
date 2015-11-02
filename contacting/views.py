from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, View

from forms import MessageForm


class Thanks(TemplateView):
    template_name = 'contacting/thanks.html'


class Contact(View):
    form_class = MessageForm
    template_name = 'contacting/contact.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(request)
            return HttpResponseRedirect(reverse('thanks'))
        return render(request, self.template_name, {'form': form})
