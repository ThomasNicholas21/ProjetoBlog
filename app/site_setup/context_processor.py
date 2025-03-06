from site_setup import models


# será inserido o context processor do aplicativo.
def testing_context_processor(request):
    return {
        'example': 'calling example '
    }

def site_setup(request):
    title = models.SiteSetup.objects.order_by('-id').first()

    return {
        'site_setup': {
            'title': title
        }
    }

