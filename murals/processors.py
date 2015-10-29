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
