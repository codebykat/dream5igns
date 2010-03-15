function setupGallery() {
  var thumbs = $('div.thumbnail', $('.thumbs'));
  thumbs.each( function(i){
    $(this).click(toggleImage);
  });

  // size filmstrip to number of photos
  var numPhotos = thumbs.size();
  //var width = thumbs.get(0).width();
  $('.thumbs').width(numPhotos*83);
  //console.info(width);
  //$('.thumbs').css('width',numPhotos*83+'px');
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
