from django.urls import path

from . import views

app_name = 'shopOnLine'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:product_id>/', views.detail, name = 'detail'),
    path('<int:product_id>/leave_comment/', views.leave_comment, name = 'leave_comment'),
]
