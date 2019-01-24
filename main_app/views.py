from django.views import generic

from .models import *


class HomeView(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['special_products'] = Product.objects.filter(special=True)
        return context


class ProductListView(generic.ListView):
    model = Product
    paginate_by = 9

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class CategoryDetailView(generic.DetailView):
    model = Category
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_template_names(self):
        if self.object.name == 'Maro mere':
            return ['maromere.html']
        else:
            return ['main_app/category_detail.html']

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)

        if self.object.name == 'Maro mere':
            context['products'] = Product.objects.filter(category__name='maromere')
            context['slides'] = Slide.objects.filter(maromere=True)
        context['categories'] = Category.objects.all()
        return context


class SubCategoryDetailView(generic.DetailView):
    model = SubCategory
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super(SubCategoryDetailView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()

        return context


class ProductDetailView(generic.DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
