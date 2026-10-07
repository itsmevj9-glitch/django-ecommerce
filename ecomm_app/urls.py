from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("login/", views.login),
    path("logout/", views.logout_page),
    path("product_list/", views.product_list, name="product_list"),
    path("add_product/", views.add_product),
    path("edit_product/", views.edit_product, name="edit_product"),
    path("view_product/", views.view_product),
    path("delete_product/", views.delete_product),
]
