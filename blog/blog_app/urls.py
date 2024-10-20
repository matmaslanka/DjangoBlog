from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add-entry', views.add_entry_view, name='add-entry'),
    path('update-entry/<slug:slug>', views.update_entry, name='update_entry'),
    path('users/register', views.register_view, name='register'),
    path('users/login', views.login_view, name='login'),
    path('users/logout', views.logout_view, name='logout'),
]
