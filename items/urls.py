from django.urls import path
from . import views

urlpatterns = [
    path('report/', views.report_lost_item, name='report_lost_item'),
    path('', views.item_list, name='item_list'),
    path('<int:item_id>/', views.item_detail, name='item_detail'),
]
