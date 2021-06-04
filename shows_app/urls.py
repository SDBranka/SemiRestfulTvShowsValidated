from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows/new', views.add_show),
    path('process_new_show', views.process_new_show),
    path('shows/<int:show_id>', views.display_show),
    path('shows', views.shows),
    path('shows/<int:show_id>/edit', views.edit_show),
    path('process_show_edit/<int:show_id>', views.process_edit), 
    path('shows/<int:show_id>/destroy', views.delete_show)
]