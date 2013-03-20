$(function() {
	var mapOptions = {
			mapTypeId: google.maps.MapTypeId.ROADMAP,
			center: new google.maps.LatLng(29.890619811136915,-97.94601621603964),
			zoom: 15,
		    scrollwheel: false,
		  }
		  var map = new google.maps.Map(document.getElementById("map"), mapOptions);
	
    var wtMarker = new google.maps.Marker({
        position: new google.maps.LatLng(29.894849073829896, -97.94601621603964),
        map: map
      });
    var campusMarker = new google.maps.Marker({
        position: new google.maps.LatLng(29.888486,-97.94421),
        map: map,
        icon: 'http://i.usatoday.net/_common/_images/_sports/logos/ncaab/texasstate_50t.png'
      });
});