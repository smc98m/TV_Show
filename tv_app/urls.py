from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.all_show),
    path('new', views.new),
    path('create_show', views.create_show),
    path('one_show/<int:id>', views.one_show),
    path('delete/<int:id>', views.destroy),
    path('shows/<int:id>', views.show),
    path('edit/<int:id>', views.edit),
    path('updated/<int:id>', views.update)
]