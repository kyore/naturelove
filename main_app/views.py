from django.http import JsonResponse
from django.urls import reverse
from django.views import generic

from .models import *

from templated_email import send_templated_mail


def send_email_view(request, product_id):
    product = Product.objects.get(id=product_id)

    if request.POST:
        phone_number = request.POST['phone_number']
        order_count = request.POST['order_count']
        total_cost = product.price * int(order_count)

        send_templated_mail(
            template_name='product_order',
            from_email='mail@naturelove.mn',
            recipient_list=['munkhuu.modiw@gmail.com', 'tjesusho@gmail.com'],
            fail_silently=False,
            context={
                'product': product,
                'phone_number': phone_number,
                'order_count': order_count,
                'total_cost': total_cost,
                'link': request.build_absolute_uri(reverse('product-detail', args=[product.pk]))
            }
        )
        return JsonResponse({'success': True})
    return JsonResponse({'valid': False})


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
