from django.shortcuts import render, redirect, get_object_or_404
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from .models import Product
from .forms import ProductForm, ProductUpdateForm

# Create your views here.
def product_create_view(request: HttpRequest) -> HttpResponse:
    context = {}
    form = ProductForm(request.POST or None)
    if (form.is_valid()):
        obj:Product = form.save(commit=False)
        if (request.user.is_authenticated):
            obj.user = request.user
            obj.save()
            return redirect("/products/create")
        else:
            form.add_error(field=None,error="Must be logged in to create")
    context['form'] = form
    return render(request, "products/create.html", context)

def product_list_view(request:HttpRequest) -> HttpResponse:
    products = Product.objects.all()
    return render(request, "products/list.html", {"products": products})

def product_detail_view(request: HttpRequest, handle:str) -> HttpResponse:
    product = get_object_or_404(Product,handle=handle)
    context = {"product":product}
    if (product.user == request.user) and (request.user.is_authenticated):
        form = ProductUpdateForm(request.POST or None, instance=product)
        if (form.is_valid()):
            obj:Product = form.save(commit=False)
            obj.save()
            # return redirect("/products/create")
        context['form'] = form
    return render(request, "products/detail.html", context)