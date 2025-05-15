from django.urls import path
from . import views

urlpatterns = [
    path('report/', views.report_lost_item, name='report_lost_item'),
]
