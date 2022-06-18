from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import View, CreateView, DeleteView, UpdateView
from .models import *
from organization.models import Tax, TransferMoney, Customer


class InvoiceList(ListView):
    model = Invoice
    paginate_by = 2
    context_object_name = 'invoices'


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['soldProducts'] = SoldProduct.objects.all()
        context['transferMoney'] = TransferMoney.objects.all()

        context['payments'] = Payment.objects.all()
        product_list = Invoice.objects.all()
        paginator = Paginator(product_list, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            file_products = paginator.page(page)
        except PageNotAnInteger:
            file_products = paginator.page(1)
        except EmptyPage:
            file_products = paginator.page(paginator.num_pages)
        context['invoices'] = file_products
        return context

    template_name = 'invoice/invoice_list.html'


# def product_view_with_category(request, slug, *args, **kwargs):
#     category = ProductCategory.objects.get(slug=slug)
#     product_categories = category.product_set.all()
#     context = {
#         'product_categories': product_categories,
#         'productInStock': ProductInStock.objects.all(),
#     }
#     return render(request, 'product/product/product_categories.html', context)
#
#
class InvoiceDetail(DetailView):
    model = Invoice
    context_object_name = 'invoice'
    template_name = 'invoice/invoice_list.html'




# class ProductCreate(CreateView):
#     model = Product
#     fields = '__all__'
#     context_object_name = 'product'
#     template_name = 'product/product/product_update.html'
#     success_url = reverse_lazy('product_list')
#
#
# class ProductUpdate(UpdateView):
#     model = Product
#     fields = '__all__'
#     context_object_name = 'product'
#     template_name = 'product/product/product_update.html'
#     success_url = reverse_lazy('product_list')
#
#
# class ProductDelete(DeleteView):
#     model = Product
#     context_object_name = 'product'
#     template_name = 'product/product/product_delete.html'
#     success_url = reverse_lazy('product_list')













class CustomerList(ListView):
    model = Customer
    paginate_by = 1
    context_object_name = 'customers'


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['soldProducts'] = SoldProduct.objects.all()
        context['transferMoney'] = TransferMoney.objects.all()

        context['payments'] = Payment.objects.all()
        product_list = Customer.objects.all()
        paginator = Paginator(product_list, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            file_products = paginator.page(page)
        except PageNotAnInteger:
            file_products = paginator.page(1)
        except EmptyPage:
            file_products = paginator.page(paginator.num_pages)
        context['invoices'] = file_products
        return context

    template_name = 'customer/customer_list.html'


# def product_view_with_category(request, slug, *args, **kwargs):
#     category = ProductCategory.objects.get(slug=slug)
#     product_categories = category.product_set.all()
#     context = {
#         'product_categories': product_categories,
#         'productInStock': ProductInStock.objects.all(),
#     }
#     return render(request, 'product/product/product_categories.html', context)
#
#
# class InvoiceDetail(DetailView):
#     model = Invoice
#     context_object_name = 'invoice'
#     template_name = 'invoice/payment_list.html'




# class ProductCreate(CreateView):
#     model = Product
#     fields = '__all__'
#     context_object_name = 'product'
#     template_name = 'product/product/product_update.html'
#     success_url = reverse_lazy('product_list')
#
#
# class ProductUpdate(UpdateView):
#     model = Product
#     fields = '__all__'
#     context_object_name = 'product'
#     template_name = 'product/product/product_update.html'
#     success_url = reverse_lazy('product_list')
#
#
# class ProductDelete(DeleteView):
#     model = Product
#     context_object_name = 'product'
#     template_name = 'product/product/product_delete.html'
#     success_url = reverse_lazy('product_list')
















class PaymentList(ListView):
    model = Payment
    paginate_by = 1
    context_object_name = 'customers'


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['soldProducts'] = SoldProduct.objects.all()
        context['transferMoney'] = TransferMoney.objects.all()

        context['payments'] = Payment.objects.all()
        product_list = Payment.objects.all()
        paginator = Paginator(product_list, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            file_products = paginator.page(page)
        except PageNotAnInteger:
            file_products = paginator.page(1)
        except EmptyPage:
            file_products = paginator.page(paginator.num_pages)
        context['invoices'] = file_products
        return context

    template_name = 'payment/payment_list.html'


# def product_view_with_category(request, slug, *args, **kwargs):
#     category = ProductCategory.objects.get(slug=slug)
#     product_categories = category.product_set.all()
#     context = {
#         'product_categories': product_categories,
#         'productInStock': ProductInStock.objects.all(),
#     }
#     return render(request, 'product/product/product_categories.html', context)
#
#
# class InvoiceDetail(DetailView):
#     model = Invoice
#     context_object_name = 'invoice'
#     template_name = 'invoice/payment_list.html'




# class ProductCreate(CreateView):
#     model = Product
#     fields = '__all__'
#     context_object_name = 'product'
#     template_name = 'product/product/product_update.html'
#     success_url = reverse_lazy('product_list')
#
#
# class ProductUpdate(UpdateView):
#     model = Product
#     fields = '__all__'
#     context_object_name = 'product'
#     template_name = 'product/product/product_update.html'
#     success_url = reverse_lazy('product_list')
#
#
# class ProductDelete(DeleteView):
#     model = Product
#     context_object_name = 'product'
#     template_name = 'product/product/product_delete.html'
#     success_url = reverse_lazy('product_list')











