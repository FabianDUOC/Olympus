class Carrito:
    def  __init__(self, request):
        self.request=request
        self.session=request.session
        carrito=self.session.get("carrito")
        if not carrito:
            carrito=self.session["carrito"]={}
        self.carrito=carrito
        
    def agregarProducto(self, producto):
        if(str(producto.idProducto) not in self.carrito.keys()):
            self.carrito[producto.idProducto]={
                "idProducto":producto.idProducto,
                "nombreProducto":producto.nombreProducto,
                "precio":str(producto.precio),
                "cantidad":1,
                "imagen":producto.foto.url,
            }
        else:
            for key, value in self.carrito.items():
                if key==str(producto.idProducto):
                    value["cantidad"]=value["cantidad"]+1
                    value["precio"]=int(value["precio"])+producto.precio
                    break
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"]=self.carrito
        self.session.modified=True

    def eliminarProducto(self, producto):
        producto.idProducto=str(producto.idProducto)
        if producto.idProducto in self.carrito:
            del self.carrito[producto.idProducto]
            self.guardar_carrito()

    def restar_producto(self, producto):
        for key, value in self.carrito.items():
            if key==str(producto.idProducto):
                    value["cantidad"]=value["cantidad"]-1
                    value["precio"]=int(value["precio"])-producto.precio
                    if value["cantidad"]<1:
                        self.eliminarProducto(producto)
                    break
        self.guardar_carrito()
    
    def limpiar_carrito(self):
        self.session["carrito"]={}
        self.session.modified=True