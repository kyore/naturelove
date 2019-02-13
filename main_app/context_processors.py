from main_app.models import Slide, Category


def get_slides(request):
    slides = Slide.objects.filter(maromere=False).order_by('-id')

    context = {
        'slides': slides
    }

    return context


def get_categories(request):
    categories = Category.objects.all()

    context = {
        'categories': categories
    }

    return context
