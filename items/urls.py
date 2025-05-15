from django.urls import path
from . import views

urlpatterns = [
    path('report/', views.report_lost_item, name='report_lost_item'),
    path('', views.item_list, name='item_list'),
    path('<int:item_id>/', views.item_detail, name='item_detail'),
    path('<int:item_id>/edit/', views.edit_item, name='edit_item'),
    path('<int:item_id>/delete/', views.delete_item, name='delete_item'),
    path('<int:item_id>/mark-returned/', views.mark_as_returned, name='mark_as_returned'),
]
