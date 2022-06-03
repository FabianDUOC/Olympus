$(document).ready(function () {
    //FORMULARIO INICIO SESIÓN
    $("#iniciar").submit(function (e) {
        e.preventDefault();

        var correo = $("#emailInicio").val();

        let msj = "";
        let entrar = false;

        $("#msjCorreo").css({ 'color': 'red' });

        if (correo.indexOf('@', 0) == -1 || correo.indexOf('.', 0) == -1) {
            msj += "El correo electrónico introducido no es válido <br>"
            entrar = true;
        }

        if (entrar) {
            $("#msjCorreo").html(msj);
        }
        else {
            Swal.fire({
                icon: 'success',
                title: 'Sesión iniciada',
                showConfirmButton: false,
                timer: 1500
              })
              $("#formRecupClave")[0].reset();
        }

    })

    // FORMULARIO RECUPERAR CONTRASEÑA
    $("#formRecupClave").submit(function (e) {
        e.preventDefault();
        var correo1 = $("#correo1").val();
        var correo2 = $("#correo2").val();

        let msj = "";
        let entrar = false;

        $("#mensajes").css({ 'color': 'red' });
        $("#mensajes").html("");

        if (correo1.indexOf('@', 0) == -1 || correo1.indexOf('.', 0) == -1 || correo2.indexOf('@', 0) == -1 || correo2.indexOf('.', 0) == -1) {
            msj += "El correo electrónico introducido no es válido <br>"
            entrar = true;
        }

        if (correo1 != correo2) {
            msj += "Los correos ingresados deben ser iguales <br>";
            entrar = true;
        }

        if (entrar) {
            $("#mensajes").html(msj);
        }
        else {
            Swal.fire({
                icon: 'success',
                title: 'Correo de recuperación enviado',
                showConfirmButton: false,
                timer: 1500
              })
            $("#formRecupClave")[0].reset();
        }
    })

    // FORMULARIO CAMBIAR CONTRASEÑA
    $("#cambiarClave").submit(function (e) {
        e.preventDefault();
        var clave = $("#claveActual").val();
        var claveNu1 = $("#claveNueva1").val();
        var claveNu2 = $("#claveNueva2").val();

        let msj = "";
        let entrar = false;

        $("#mensajes").css({ 'color': 'red' });
        $("#mensajes").html("");

        if (claveNu1.trim().length < 6) {
            msj += "La contraseña nueva de tener al menos 6 caracteres <br>";
            entrar = true;
        }
        if (claveNu1 == clave) {
            msj += "Las contraseñas nuevas deben ser distinta a la contraseña antigua <br>"
            entrar = true;
        }
        if (claveNu1 != claveNu2) {
            msj += "Las contraseñas nuevas deben ser iguales <br>"
            entrar = true;
        }


        if (entrar) {
            $("#mensajes").html(msj);
        }
        else {
            Swal.fire({
                icon: 'success',
                title: 'Contraseña cambiada exitósamente',
                showConfirmButton: false,
                timer: 1500
              })

            $("#cambiarClave")[0].reset();
        }
    })

    // FORMNULARIO CONTÁCTANOS
    $("#formContanto").submit(function (e) {


        var nom = $("#nombre").val();
        var correo = $("#email").val();

        let msj = "";
        let entrar = false;

        $("#mensajes2").html("");
        $("#msjCorreo").html("");

        if (nom.trim().length < 4 || nom.trim().length > 10) {
            msj += "El nombre no tiene la longitud válida <br>";
            entrar = true;
        }

        if (correo.indexOf('@', 0) == -1 || correo.indexOf('.', 0) == -1) {
            $("#msjCorreo").html("El correo electrónico introducido no es válido");
            entrar = true;
        }

        if (entrar) {
            $("#mensajes1").html(msj);
            e.preventDefault();
        }
        else {
            $("#mensajes1").html("");
            $("#mensajes2").css({ 'color': 'blue' });
            $("#mensajes2").html("Mensaje enviado exitosamente");
            $("#formContanto")[0].reset();
        }
    })

    // FORMULARIO REGISTRO DE CUENTA
    $("#formRegistro").submit(function (e) {
        e.preventDefault();

        var nom = $("#nombre").val();
        var apellidoPa = $("#apellidoPa").val();
        var apellidoMa = $("#apellidoMa").val();
        var email = $("#correoRegistro").val();
        var direcc = $("#direccion").val();
        var region = $("#region").val();
        var comuna = $("#comuna").val();
        var numTel = $("#telefono").val();
        var clave1 = $("#clave1").val();
        var clave2 = $("#clave2").val();

        let entrar = false;
        let msjClaves = "";

        $("#msjNom").html("");
        $("#msjApellidoPa").html("");
        $("#msjApellidoMa").html("");
        $("#msjCorreo").html("")
        $("#msjDireccion").html("");
        $("#msjRegion").html("");
        $("#msjComuna").html("");
        $("#msjTel").html("");
        $("#msjClave").html("");

        $("#msj").html("");

        if (nom.trim().length < 4 || nom.trim().length > 10) {
            $("#msjNom").html("El nombre no tiene la longitud válida");
            entrar = true;
        }

        if (apellidoPa.trim().length < 4 || apellidoPa.trim().length > 10) {
            $("#msjApellidoPa").html("El apellido no tiene la longitud válida");
            entrar = true;
        }

        if (apellidoMa.trim().length < 4 || apellidoMa.trim().length > 10) {
            $("#msjApellidoMa").html("El apellido no tiene la longitud válida");
            entrar = true;
        }

        if (email.indexOf('@', 0) == -1 || email.indexOf('.', 0) == -1) {
            $("#msjCorreo").html("El correo electrónico introducido no es válido")
        }

        if (direcc.trim().length < 4) {
            $("#msjDireccion").html("La dirección debe tener al menos 4 caracteres");
            entrar = true;
        }

        if (region == "Escoge tu Región") {
            $("#msjRegion").html("Seleccionar región")
            entrar = true;
        }

        if (numTel.trim().length != 11) {
            $("#msjTel").html("Numero de telefono de 11 dígitos");
            entrar = true;
        }

        if (comuna == "Escoge tu Comuna") {
            $("#msjComuna").html("Seleccionar comuna")
            entrar = true;
        }

        if (clave1.trim().length < 6) {
            msjClaves += "La contraseña de tener al menos 6 caracteres <br>";
            entrar = true;
        }

        if (clave1 != clave2) {
            msjClaves += "Las contraseñas deben ser iguales";
            entrar = true;
        }

        if (entrar) {
            $("#msjClave").html(msjClaves);
        }
        else {
            Swal.fire({
                icon: 'success',
                title: 'Cuenta creada exitosamente',
                showConfirmButton: false,
                timer: 1500
              })
            $("#formRegistro")[0].reset();
        }
    })

    // FORMULARIO EDITAR CUENTA
    $("#editCuenta").submit(function (e) {
        e.preventDefault();

        var nom = $("#nombre").val();
        var apellidoPa = $("#apellidoPa").val();
        var apellidoMa = $("#apellidoMa").val();
        var direcc = $("#direccion").val();
        var region = $("#region").val();
        var comuna = $("#comuna").val();
        var numTel = $("#telefono").val();

        let entrar = false;

        $("#msjNom").html("");
        $("#msjApellidoPa").html("");
        $("#msjApellidoMa").html("");
        $("#msjDireccion").html("");
        $("#msjRegion").html("");
        $("#msjComuna").html("");
        $("#msjTel").html("");

        $("#msj").html("");

        if (nom.trim().length < 4 || nom.trim().length > 10) {
            $("#msjNom").html("El nombre no tiene la longitud válida");
            entrar = true;
        }

        if (apellidoPa.trim().length < 4 || apellidoPa.trim().length > 10) {
            $("#msjApellidoPa").html("El apellido no tiene la longitud válida");
            entrar = true;
        }

        if (apellidoMa.trim().length < 4 || apellidoMa.trim().length > 10) {
            $("#msjApellidoMa").html("El apellido no tiene la longitud válida");
            entrar = true;
        }

        if (direcc.trim().length < 4) {
            $("#msjDireccion").html("La dirección debe tener al menos 4 caracteres");
            entrar = true;
        }

        if (region == "Escoge tu Región") {
            $("#msjRegion").html("Seleccionar región")
            entrar = true;
        }

        if (numTel.trim().length != 11) {
            $("#msjTel").html("Numero de telefono de 11 dígitos");
            entrar = true;
        }

        if (comuna == "Escoge tu Comuna") {
            $("#msjComuna").html("Seleccionar comuna")
            entrar = true;
        }

        if (entrar) {
        }
        else {
            Swal.fire({
                icon: 'success',
                title: 'Se han guardado los cambios',
                showConfirmButton: false,
                timer: 1500
              })
        }
    })

    // FORMULARIO AGREGAR PRODUCTO
    $("#agregarP").submit(function (e) {

        var nombre = $("#nombreProducto").val();
        var precio = $("#precioP").val();
        var desCorta = $("#descripcionCorta").val();
        var desLarga = $("#descripcionDetallada").val();
        var cantidad = $("#cantidad").val();
        var categoria = $("#categoria").val();

        $("#msjNombre").html("");
        $("#msjPrecio").html("");
        $("#msjCorta").html("");
        $("#msjDetallada").html("");
        $("#msjCantidad").html("");
        $("#msjCategorias").html("");

        $("#msj").html("");

        let entrar = false;

        if (nombre.trim().length < 4 || nombre.trim().length > 15) {
            $("#msjNombre").html("El nombre de producto no tiene la longitud válida");
            entrar = true;
        }

        if (precio == 0) {
            $("#msjPrecio").html("Precio debe ser mayor a 0")
            entrar = true;
        }

        if (desCorta.trim().length < 4 || desCorta.trim().length > 20) {
            $("#msjCorta").html("La descripción no tiene la longitud válida");
            entrar = true;
        }

        if (desLarga.trim().length < 10 || desLarga.trim().length > 200) {
            $("#msjDetallada").html("La descripción no tiene la longitud válida");
            entrar = true;
        }

        if (cantidad == 0) {
            $("#msjCantidad").html("Cantidad debe ser mayor a 0")
            entrar = true;
        }

        if (categoria == "Categoría") {
            $("#msjCategorias").html("Debe seleccionar una categoría")
            entrar = true;
        }

        if (entrar) {
            e.preventDefault();
        }
        else {
        
        }
    })

    // FORMULARIO EDITAR PRODUCTO
    $("#editarP").submit(function (e) {
        e.preventDefault();

        var nombre = $("#nombreProducto").val();
        var precio = $("#precioP").val();
        var desCorta = $("#descripcionCorta").val();
        var desLarga = $("#descripcionDetallada").val();
        var cantidad = $("#cantidad").val();
        var categoria = $("#categoria").val();

        $("#msjNombre").html("");
        $("#msjPrecio").html("");
        $("#msjCorta").html("");
        $("#msjDetallada").html("");
        $("#msjCantidad").html("");
        $("#msjCategorias").html("");

        $("#msj").html("");

        let entrar = false;

        if (nombre.trim().length < 4 || nombre.trim().length > 15) {
            $("#msjNombre").html("El nombre de producto no tiene la longitud válida");
            entrar = true;
        }

        if (precio == 0) {
            $("#msjPrecio").html("Precio debe ser mayor a 0")
            entrar = true;
        }

        if (desCorta.trim().length < 4 || desCorta.trim().length > 20) {
            $("#msjCorta").html("La descripción no tiene la longitud válida");
            entrar = true;
        }

        if (desLarga.trim().length < 10 || desLarga.trim().length > 200) {
            $("#msjDetallada").html("La descripción no tiene la longitud válida");
            entrar = true;
        }

        if (cantidad == 0) {
            $("#msjCantidad").html("Cantidad debe ser mayor a 0")
            entrar = true;
        }

        if (categoria == "Categoría") {
            $("#msjCategorias").html("Debe seleccionar una categoría")
            entrar = true;
        }

        if (entrar) {
        }
        else {
            Swal.fire({
                icon: 'success',
                title: 'Información de producto modificada',
                showConfirmButton: false,
                timer: 1500
              })
        }
    })


    // FORMULARIO MENSAJES ADMIN
    $("#formMensaje").submit(function (e) {
        e.preventDefault();
        Swal.fire({
            icon: 'success',
            title: 'Mensaje enviado satisfactoriamente',
            showConfirmButton: false,
            timer: 1500
          })
        $("#formMensaje")[0].reset();
    })

    // FORMULARIO FOOTER
    $("#suscripcion").submit(function(e){
        

        var correo = $("#emailF").val();

        $("#mensajes").html("")
        
        let entrar = false;

        if (correo.indexOf('@', 0) == -1 || correo.indexOf('.', 0) == -1) {
            $("#mensajes").html("El correo electrónico introducido no es válido")
            entrar = true;
        }

        if (entrar) {
        }
        else {
            Swal.fire({
                icon: 'success',
                title: 'Usted se ha suscrito Correctamente',
                showConfirmButton: false,
                timer: 1500
              })
            $("#suscripcion")[0].reset();
        }

    })


})