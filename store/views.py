from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import View,  CreateView, DeleteView, UpdateView
from .models import *
from organization.models import Tax


def storeView(request):
    return render(request, 'home/index.html')



def timeView(requset):
    context = {}
    context['productInStock'] = ProductInStock.objects.all()
    context['products'] = Product.objects.all()

    return render(requset, 'home/time.html', context)







class ProductList(ListView):
    model = Product
    paginate_by = 2
    context_object_name = 'products'

    def get_context_data(self, *args,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['productInStock'] = ProductInStock.objects.all()
        context['productCategory'] = ProductCategory.objects.all()
        product_list = Product.objects.all()
        paginator = Paginator(product_list, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            file_products = paginator.page(page)
        except PageNotAnInteger:
            file_products = paginator.page(1)
        except EmptyPage:
            file_products = paginator.page(paginator.num_pages)
        context['file_products'] = file_products
        return context

    template_name = 'product/product/product_list.html'




def product_view_with_category(request, slug, *args, **kwargs):
    category = ProductCategory.objects.get(slug=slug)
    product_categories = category.product_set.all()
    context = {
        'product_categories': product_categories,
        'productInStock': ProductInStock.objects.all(),
    }
    return render(request, 'product/product/product_categories.html', context)


class ProductDetail(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'product/product/product_detail.html'





class ProductCreate(CreateView):
    model = Product
    fields = '__all__'
    context_object_name = 'product'
    template_name = 'product/product/product_update.html'
    success_url = reverse_lazy('product_list')




class ProductUpdate(UpdateView):
    model = Product
    fields = '__all__'
    context_object_name = 'product'
    template_name = 'product/product/product_update.html'
    success_url = reverse_lazy('product_list')





class ProductDelete(DeleteView):
    model = Product
    context_object_name = 'product'
    template_name = 'product/product/product_delete.html'
    success_url = reverse_lazy('product_list')
















class ProductInStockList(ListView):
    model = ProductInStock
    paginate_by = 2
    context_object_name = 'file_products'

    def get_context_data(self, *args,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['productInStock'] = ProductInStock.objects.all()
        context['productCategory'] = ProductCategory.objects.all()
        product_list = ProductInStock.objects.all()
        paginator = Paginator(product_list, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            file_products = paginator.page(page)
        except PageNotAnInteger:
            file_products = paginator.page(1)
        except EmptyPage:
            file_products = paginator.page(paginator.num_pages)
        context['file_products'] = file_products
        return context

    template_name = 'product/inStock/stock_list.html'


class ProductInStockCreate(CreateView):
    model = ProductInStock
    fields = '__all__'
    context_object_name = 'product'
    template_name = 'product/product/product_update.html'
    success_url = reverse_lazy('stock_list')





class StockUpdate(UpdateView):
    model = ProductInStock
    fields = '__all__'
    context_object_name = 'product'
    pk_url_kwarg = 'id'
    template_name = 'product/inStock/stock_update.html'
    success_url = reverse_lazy('stock_list')




class StockDelete(DeleteView):
    model = ProductInStock
    context_object_name = 'product'
    pk_url_kwarg = 'id'
    template_name = 'product/inStock/stock_delete.html'
    success_url = reverse_lazy('stock_list')














class CategoryList(ListView):
    model = ProductCategory
    paginate_by = 10
    context_object_name = 'categories'

    def get_context_data(self, *args,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['productCategory'] = ProductCategory.objects.all()
        product_list = ProductCategory.objects.all()
        paginator = Paginator(product_list, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            file_products = paginator.page(page)
        except PageNotAnInteger:
            file_products = paginator.page(1)
        except EmptyPage:
            file_products = paginator.page(paginator.num_pages)
        context['categories'] = file_products
        return context

    template_name = 'product/category/category_list.html'


class CategoryCreate(CreateView):
    model = ProductCategory
    fields = '__all__'
    template_name = 'product/category/category_update.html'
    success_url = reverse_lazy('category_list')





class CategoryUpdate(UpdateView):
    model = ProductCategory
    fields = '__all__'
    pk_url_kwarg = 'id'
    template_name = 'product/category/category_update.html'
    success_url = reverse_lazy('category_list')




class CategoryDelete(DeleteView):
    model = ProductCategory
    context_object_name = 'category'
    pk_url_kwarg = 'id'
    template_name = 'product/category/category_delete.html'
    success_url = reverse_lazy('category_list')



















class TaxList(ListView):
    model = Tax
    paginate_by = 1
    context_object_name = 'taxs'

    def get_context_data(self, *args,  **kwargs):
        context = super().get_context_data(**kwargs)
        # context['productCategory'] = ProductCategory.objects.all()
        product_list = Tax.objects.all()
        paginator = Paginator(product_list, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            file_products = paginator.page(page)
        except PageNotAnInteger:
            file_products = paginator.page(1)
        except EmptyPage:
            file_products = paginator.page(paginator.num_pages)
        context['taxs'] = file_products
        return context

    template_name = 'product/tax/tax_list.html'


class TaxCreate(CreateView):
    model = Tax
    fields = '__all__'
    template_name = 'product/tax/tax_update.html'
    success_url = reverse_lazy('tax_list')





class TaxUpdate(UpdateView):
    model = Tax
    fields = '__all__'
    pk_url_kwarg = 'id'
    template_name = 'product/tax/tax_update.html'
    success_url = reverse_lazy('tax_list')




class TaxDelete(DeleteView):
    model = Tax
    context_object_name = 'tax'
    pk_url_kwarg = 'id'
    template_name = 'product/tax/tax_delete.html'
    success_url = reverse_lazy('tax_list')











