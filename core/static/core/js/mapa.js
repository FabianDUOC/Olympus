function iniciarMapa(){
    var coordenada = {lat:-33.3827021 ,lng:-70.6612942};
    var mapa = new google.maps.Map(document.getElementById('mapa'),{
      zoom: 18,
      center: coordenada
    });
    var marker = new google.maps.Marker({
      position: coordenada,
      map: mapa
    });
}