from carrito.carrito import Carrito

def total_carrito(request):
    carrito= Carrito(request)
    total=0
    despacho=5000
    #if request.user.is_authenticated:
    for key,value in request.session["carrito"].items():
            total=total+(int(value["precio"]))
    return {"total_carrito":total,"despacho":despacho}