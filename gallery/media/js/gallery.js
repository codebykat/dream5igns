function setupGallery() {
  $('div.thumbnail').each( function(i){
    $(this).click(toggleImage);
  });
}

function toggleImage() {
  var id = this.id.substr(10);
  var photo_id = "photo-" + id;
  console.info(photo_id);
  console.info($('div[id='+photo_id+']'));
  //alert($('div[id=photo_id]'));
  $('div.photo:visible').hide();
  $('#'+photo_id).show();
}

jQuery(setupGallery());
//$(document).ready(setupGallery());
