from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate, login as auth_login
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("dashboard")
        else:
            return render(request, "login.html")
    return render(request, "login.html")


def logout_page(request):
    logout(request)
    return redirect("/login/")


@login_required
def dashboard(request):
    products = Product.objects.all()
    total = products.count()
    active = products.filter(status=True).count()
    inactive = products.filter(status=False).count()
    low_stock = products.filter(stock__lte=5).count()
    return render(
        request,
        "dashboard.html",
        {
            "total": total,
            "active": active,
            "inactive": inactive,
            "low_stock": low_stock,
        },
    )


def product_list(request):
    products = Product.objects.all()
    return render(request, "product_list.html", {"products": products})


@login_required
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm()

    return render(request, "product_form.html", {"form": form})


@login_required
def edit_product(request):
    id = request.GET.get("id")
    product = get_object_or_404(Product, id=id)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()
            return redirect("product_list")

    else:
        form = ProductForm(instance=product)

    return render(request, "product_form.html", {"form": form})


def view_product(request):
    id = request.GET.get("id")
    product = get_object_or_404(Product, id=id)
    return render(request, "product_detail.html", {"product": product})


@login_required
def delete_product(request):
    id = request.GET.get("id")
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect("product_list")
