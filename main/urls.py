from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('insert_wish/', views.insert_wish, name="insert_wish"),
    path('delete/<int:item_id>/', views.delete, name='delete'),

]