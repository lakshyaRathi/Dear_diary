from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add', views.add, name='add'),
    path('delete/<int:entry_id>/', views.delete_entry, name='delete'),
    path('edit/<int:entry_id>/', views.edit_entry, name='edit'),
    path('detail/<int:entry_id>/', views.detail_entry, name='detail'),
]
