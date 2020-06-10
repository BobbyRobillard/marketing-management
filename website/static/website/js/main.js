var admin_email = "admin@techandmech.com";
//------------------------------------------------------------------------------
// For items that direct a user somewhere. I.e: trashcan (delete), pencil (edit)
//------------------------------------------------------------------------------
$('body').on('click', '.action-link', function(e) {
    e.stopPropagation();
    window.location.href = $(this).attr('href');
});
//------------------------------------------------------------------------------
// Filtering Method
//------------------------------------------------------------------------------
function filter_cards(to_show) {
  $('.item-container').each(function() {
    $(this).css('display', 'none');
  });
  for(i=0; i < to_show.length; i++) {
    $('.' + to_show[i]).css('display', 'inline');
  }
}

function set_active(obj, default_class) {
  $('.' + default_class).each(function() {
    $(this).addClass('btn-default');
  });
  $(obj).removeClass('btn-default');
  $(obj).addClass('btn-primary');
}
//------------------------------------------------------------------------------
// Search Functionality
//------------------------------------------------------------------------------
$('#search').keyup(function(e) {
  var search_val = $(this).val().toLowerCase();
  if(search_val.length == 0) {
    $('.item-container').each(function() {
      $(this).css('display', 'inline');
    })
  }
  else {
    $('.item-container').each(function() {
      var item_val = $(this).html().toLowerCase();
      console.log("IV: " + item_val + "\n");
      if(! item_val.includes(search_val)) {
        $(this).css('display', 'none')
      }
    });
  }
});
//------------------------------------------------------------------------------
// Real Time Updates Bar
//------------------------------------------------------------------------------
// const playModeSocket = new WebSocket(
//     'ws://'
//     + '192.168.50.201:8000'
//     + '/ws/macros/'
//     + 'updates/'
// );
//
// playModeSocket.onmessage = function(e) {
//     const data = JSON.parse(e.data);
//     $("#play-mode").prop('checked', data.playMode);
//     $("#recording").prop('checked', data.isRecording);
//
// };
//
// playModeSocket.onclose = function(e) {
//     console.error('Chat socket closed unexpectedly');
// };
//------------------------------------------------------------------------------
// Convert Hex Color to opacity
//------------------------------------------------------------------------------
function convertHex(hex, opacity){
  return 'rgba(' + parseInt(hex.slice(-6, -4), 16)
        + ',' + parseInt(hex.slice(-4, -2), 16)
        + ',' + parseInt(hex.slice(-2), 16)
        +',' + opacity + ')';
}
//------------------------------------------------------------------------------
