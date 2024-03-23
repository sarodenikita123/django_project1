from django.urls import path
from .views import create_order, show_order, update_order, delete_order


urlpatterns = [
    path("create/", create_order, name='create_url'),
    path("show/", show_order, name='show_url'),
    path("update/<int:pk>/", update_order, name='update_url'),
    path("delete/<int:pk>/", delete_order, name='delete_url')
]