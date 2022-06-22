from django.urls import path
from api_rest.views import (listaProductos, agregarProducto, controlProducto,
                            listaCategorias, agregarCategoria, 
                            listaRegiones, 
                            listaComunas)
from api_rest.viewsLogin import login

urlpatterns = [
    path('listaProductos/',listaProductos,name="listaProductos"),
    path('agregarProducto/',agregarProducto,name="agregarProducto"),
    path('controlProducto/<idP>/',controlProducto,name="controlProducto"),
    path('listaCategorias/',listaCategorias,name="listaCategorias"),
    path('agregarCategoria/',agregarCategoria,name="agregarCategoria"),
    path('listaRegiones/',listaRegiones,name="listaRegiones"),
    path('listaComunas/',listaComunas,name="listaComunas"),
    path('login/',login,name="login"),
]