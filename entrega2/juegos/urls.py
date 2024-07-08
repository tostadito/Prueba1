from django.urls import path
from . import views
from .views import crud_view


urlpatterns = [
    path('', views.index, name='index'),
    path('browse', views.browse, name='browse'),
    path('details', views.details, name='details'),
    path('profile', views.profile, name='profile'),
    path('streams', views.streams, name='streams'),
    path('crud', views.crud, name='crud'),
    path('crud_find/<str:pk>', views.crud_find, name='crud_find'),
    path('crud_add', views.crud_add, name='crud_add'),
    path('crud_edit', views.crud_edit, name='crud_edit'),
    path('crud_delete/<str:pk>', views.crud_delete, name='crud_delete'),
    path('crud_genero', views.crud_genero, name='crud_genero'),
    path('user_add', views.user_add, name='user_add'),
    path('user_update', views.user_update, name='user_update'),

]