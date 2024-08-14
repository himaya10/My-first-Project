from django.urls import path
from . import views

urlpatterns = [
    path('Category/', views.Category_view),
    path('unit/',views.unit_view),
    path('item/',views.item_view),
    path('supplier/', views.supplier_view),
    path('order/', views.order_view),
]