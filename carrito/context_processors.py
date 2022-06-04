from carrito.carrito import Carrito

def total_carrito(request):
    carrito= Carrito(request)
    total=0
    #if request.user.is_authenticated:
    for key,value in request.session["carrito"].items():
            total=total+(int(value["precio"])*value["cantidad"])
    return {"total_carrito":total}