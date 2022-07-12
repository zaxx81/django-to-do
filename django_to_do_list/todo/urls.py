from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_list, name='list'),
    path('list/', views.view_list, name='list'),
    path('new/', views.new, name="new"),
    # path('show/<item_id>', views.item_show),
    # path('item_create/', views.item_create),
    # path('item_edit/', views.item_edit),
    # path('item_update/', views.item_update),
    # path('item_destroy/', views.item_destroy),
]