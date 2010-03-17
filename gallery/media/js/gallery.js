function setupGallery() {
  var thumbs = $('div.thumbnail', $('.thumbs'));
  thumbs.each( function(i){
    $(this).click(toggleImage);
  });

  // size filmstrip to number of photos
  var numPhotos = thumbs.size();
  var width = thumbs.outerWidth(true);
  $('.thumbs').width(numPhotos*width);
}

function toggleImage() {
  var id = this.id.substr(10);
  var photo_id = "photo-" + id;
  $('div.photo:visible').hide();
  $('#'+photo_id).show();
}

function scrollStrip(multiplier) {
  // multiplier -1 will scroll left, 1 will scroll right

  var photoWidth = 83;
  var scroll = photoWidth * multiplier;

  var scrollGoal = $('#photostrip').scrollLeft() + scroll;
  $('#photostrip').animate({scrollLeft: scrollGoal}, 200);
}

function setupScroll() {
  $('#navleft').click(function() {scrollStrip(-1);});
  $('#navright').click(function() {scrollStrip(1);});
}

jQuery(setupGallery());
jQuery(setupScroll());
//$(document).ready(setupGallery());
