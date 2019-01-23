from main_app.models import Slide


def get_slides(request):
    slides = Slide.objects.all().order_by('-id')

    context = {
        'slides': slides
    }

    return context
