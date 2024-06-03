from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # prima pagina

    path('collezione/', views.collezione, name='collezione'),  # base_generic, prodotti_coll_tipo
    path('collezione/<pk>', views.collezione_detail, name='collezione-detail'),
                                #collezione_list, prodotti_coll_tipo
    path('catalogo/', views.catalogo, name='catalogo'), #index, ? catalogo_detail
    path('catalogo/<pk>', views.catalogo_detail, name='catalogo-detail'), #catalogo_list, prodotti_coll_tipo
    path('catalogo/<pk>/<coll>', views.catalogo_detail_collezione, name='catalogo-detail-collezione'), #collezione_list
    path('catalogo/<pk>/<pagina>/<book>', views.catalogo_book, name='catalogo-book'), #catalogo book

    path('tipo/', views.tipo, name='tipo'), #index, prodotti_coll_tipo
    path('tipo/<pk>', views.tipo_detail, name='tipo-detail'), #tipo_list

    path('prodotto/<pk>/<set>/<url_id>', views.prodotto, name='prodotto'), # prodotti_coll_tipo

    path('progetto/', views.progetto_, name='progetto_'),
    path('progetto/<stanza>', views.progetto, name='progetto'), # base_generic,
    path('progetto/<stanza>/<pk>', views.progetto_detail, name='progetto-detail'), #progetto_list

    path('elenco/<sort>/<coll_pk>', views.elenco, name='elenco'), # elenco,

]