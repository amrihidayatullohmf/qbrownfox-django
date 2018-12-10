function initMap() {
  var myLatLng = {lat: -25.363, lng: 131.044};

  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 4,
    center: myLatLng
  });

  var marker = new google.maps.Marker({
    position: myLatLng,
    map: map,
    title: 'Hello World!'
  });
}

$(document).ready(function(){
  $(window).scroll(function () {
    var pos = $(this).scrollTop();
    if(pos > 100) {
      $("header").addClass('on');
    } else {
      $("header").removeClass('on');
    }
  });

  $("#guestbookform").submit(function(){
    var ldr = $(this).find('.ldr');
    var sbt = $(this).find('.sbt');
    var _self = $(this);

    ldr.show();
    sbt.hide();

    $.ajax({
      type : 'post',
      url : $(this).attr('action'),
      data : $(this).serialize(),
      dataType : 'json',
      success : function(d) {
        console.log(d.code);
        ldr.hide();
        sbt.show();
        _self.find('input').val('');
      },
      error : function(e) {
        console.log(e)
        ldr.hide();
        sbt.show();
      }
    });

    return false;
  });
});
