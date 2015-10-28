from showing.models import Gallery


def navbar(request):
    '''
    Adds the needed data for the navbar context
    '''
    if not request.resolver_match.kwargs:
        slug = None             # TODO: I'm not sure about
    else:                       # this at all.
        slug = request.resolver_match.kwargs.pop('slug', None)

    return {'navbar': {'galleries': Gallery.objects.as_navbar(),
                       'active': slug}}
