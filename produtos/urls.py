from xml.dom.minidom import Document
from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name="index"),
    path('produtos/', views.produtos, name="produtos"),
    path('categorias/', views.categorias, name="categorias"),
    path('sobre/', views.sobre, name="sobre"),
    path('add_produto/', views.add_produto, name="add_produto"),
    path('edit_produto/<int:produto_id>', views.edit_produto, name="edit_produto"),
    path('del_produto/<int:produto_id>', views.del_produto, name="del_produto"),
    path('delete-categoria/<int:categoria_id>', views.deleteCategoria, name='delete-categoria'),
    path('edit_categoria/<int:categoria_id>', views.edit_categoria, name="edit_categoria"),
    path('add_categoria/', views.add_categoria, name="add_categoria"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


