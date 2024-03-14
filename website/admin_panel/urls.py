from django.urls import path
from . import views

urlpatterns = [
    path('',views.admin_home ,name='home'),
    path('admin_user/',views.admin_user ,name='admin_user'),
    path("<int:id>/blockuser/", views.blockuser, name="blockuser"),
    path("<int:id>/usersprofile/", views.usersprofile, name="usersprofile"),
    path('<int:id>/toggle_admin/', views.toggle_admin, name='toggle_admin'),
    

    path('admin_category/',views.admin_category ,name='admin_category'),
    path("<add_Category/", views.add_Category, name="add_Category"),
    path("<str:slug>/<edit_Category/", views.edit_Category, name="edit_Category"),
    path("<str:slug>/delete_Category/", views.delete_Category, name="delete_Category"),
    
    path('admin_products/',views.admin_products ,name='admin_products'),
    path("add_Product/", views.add_Product, name="add_Product"),
    path("<int:id>/edit_Product/", views.edit_Product, name="edit_Product"),
    path("<int:id>/delete_Product/", views.delete_Product, name="delete_Product"),
    
    path('admin_orders/',views.admin_orders ,name='admin_orders'),
    
]