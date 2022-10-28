from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('produtos/', views.produtos, name="produtos"),
    path('categorias/', views.categorias, name="categorias"),
    path('sobre/', views.sobre, name="sobre"),
    path('add_produto/', views.add_produto, name="add_produto"),
    path('edit_produto/<int:produto_id>', views.edit_produto, name="edit_produto"),
    path('del_produto/<int:produto_id>', views.del_produto, name="del_produto"),
]



