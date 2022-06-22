from django.urls import path
from api_rest.views import agregarProducto, controlProducto, listaProductos, agregarCategoria, listaCategorias, listaRegiones, listaComunas
from api_rest.viewsLogin import login

urlpatterns = [
    path('agregarProducto/',agregarProducto,name="agregarProducto"),
    path('controlProducto/<idP>/',controlProducto,name="controlProducto"),
    path('listaProductos/',listaProductos,name="listaProductos"),
    path('listaCategorias/',listaCategorias,name="listaCategorias"),
    path('agregarCategoria/',agregarCategoria,name="agregarCategoria"),
    path('listaRegiones/',listaRegiones,name="listaRegiones"),
    path('listaComunas/',listaComunas,name="listaComunas"),
    path('login/',login,name="login"),
]