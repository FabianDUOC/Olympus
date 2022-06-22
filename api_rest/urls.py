from django.urls import path
from api_rest.views import (listaProductos, agregarProducto, controlProducto,
                            listaCategorias, agregarCategoria, controlCategoria, 
                            listaRegiones, agregarRegion, controlRegion,
                            listaComunas, agregarComuna, controlComuna)
from api_rest.viewsLogin import login

urlpatterns = [
    path('listaProductos/',listaProductos,name="listaProductos"),
    path('agregarProducto/',agregarProducto,name="agregarProducto"),
    path('controlProducto/<idP>/',controlProducto,name="controlProducto"),

    path('listaCategorias/',listaCategorias,name="listaCategorias"),
    path('agregarCategoria/',agregarCategoria,name="agregarCategoria"),
    path('controlCategoria/<idC>/',controlCategoria,name="controlCategoria"),

    path('listaRegiones/',listaRegiones,name="listaRegiones"),
    path('agregarRegion/',agregarRegion,name="agregarRegion"),
    path('controlRegion/<idR>/',controlRegion,name="controlRegion"),

    path('listaComunas/',listaComunas,name="listaComunas"),
    path('agregarComuna/',agregarComuna,name="agregarComuna"),
    path('controlComuna/<idC>/',controlComuna,name="controlComuna"),

    path('login/',login,name="login"),
]