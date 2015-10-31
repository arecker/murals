from django.conf import settings

from showing.models import Gallery


def navbar(request):
    '''
    Adds the needed data for the navbar context
    '''
    return {
        'navbar': {
            'galleries': Gallery.objects.all()
        }
    }


def analytics(request):
    '''
    Inject google analytics tracking code into context
    '''
    ga_prop_id = getattr(settings, 'GOOGLE_ANALYTICS_PROPERTY_ID', False)
    if not settings.DEBUG and ga_prop_id:
        return {
            'GOOGLE_ANALYTICS_PROPERTY_ID': ga_prop_id,
        }
    return {}
