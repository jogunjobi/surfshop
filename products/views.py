from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Product, Profile
from products.forms import ProductForm
from django.contrib.auth.forms import UserCreationForm


def vendor_registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # # Set user type to vendor
            # Profile.objects.create(user=user, user_type='vendor')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/vendor_registration.html', {'form': form})


@login_required
def redirect_user(request):
    if request.user.profile.user_type == 'admin':
        return redirect('admin_all_products')
    elif request.user.profile.user_type == 'vendor':
        return redirect('vendor_all_products')


@login_required
def product_upload(request):
    user_profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = user_profile
            product.save()
            return redirect('vendor_all_products')
    else:
        form = ProductForm()
    return render(request, 'products/product_upload.html', {'form': form})


@login_required
def admin_product_approval(request):
    if not request.user.profile.user_type == 'admin':
        return redirect('redirect_user')

    pending_products = Product.objects.filter(status=Product.PENDING)

    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        product.status = Product.APPROVED
        product.save()
        return redirect('admin_product_approval')

    return render(request, 'products/product_approval.html', {'pending_products': pending_products})


@login_required
def admin_all_products(request):
    if not request.user.profile.user_type == 'admin':
        return redirect('redirect_user')

    all_products = Product.objects.all().order_by('-create_date')
    return render(request, 'products/products.html', {'all_products': all_products})


@login_required
def admin_product_detail(request, product_uuid):
    if not request.user.profile.user_type == 'admin':
        return redirect('redirect_user')

    product = Product.objects.get(product_uuid=product_uuid)

    if request.method == 'POST':
        product_uuid = request.POST.get('product_id')
        product = get_object_or_404(Product, product_uuid=product_uuid)
        product.status = Product.APPROVED
        product.save()
        return redirect('admin_product_approval')

    context = {
        "product": product
    }
    return render(request, 'products/product_detail.html', context)


@login_required
def vendor_all_products(request):
    all_products = Product.objects.filter(vendor__user=request.user).order_by('-create_date')

    context = {
        'all_products': all_products
    }

    return render(request, 'products/products.html', context)


@login_required
def vendor_product_detail(request, username, product_uuid):
    vendor_instance = Profile.objects.get(user__username=username)
    product = Product.objects.get(vendor=vendor_instance,
                                  product_uuid=product_uuid)
    context = {
        "product": product
    }
    return render(request, 'products/product_detail.html', context)

