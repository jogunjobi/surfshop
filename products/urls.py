from django.urls import include, path
from django.views.generic import TemplateView, View, CreateView
from django.contrib.auth.decorators import login_required
from products.views import (product_upload,
                            admin_product_approval,
                            admin_all_products,
                            admin_product_detail,
                            vendor_all_products,
                            vendor_product_detail)

urlpatterns = [
    path('product/upload/', product_upload, name='product_upload'),
    path('products/approval/', admin_product_approval, name='admin_product_approval'),
    path('products/all/', admin_all_products, name='admin_all_products'),
    path('product/<str:product_uuid>', admin_product_detail, name='admin_product_detail'),
    path('products/', vendor_all_products, name='vendor_all_products'),
    path('product/<username>/<str:product_uuid>', vendor_product_detail, name='vendor_product_detail')
]
