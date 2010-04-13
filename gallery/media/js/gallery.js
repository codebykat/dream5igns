/* gallery stuff */
function setupGallery() {
  var thumbs = $('div.thumbnail', $('#thumbs'));
  thumbs.each( function(i){
    $(this).click(toggleImage);
  });

  // size filmstrip to number of photos
  var numPhotos = thumbs.size();
  var width = thumbs.outerWidth(true);
  $('#thumbs').width(numPhotos*width);
}

function toggleImage() {
  var id = this.id.substr(10);
  var photo_id = "photo-" + id;
  $('div.photo:visible').hide();
  $('#'+photo_id).show();
}
jQuery(setupGallery());

/* filmstrip scrolling */
function scrollStrip(multiplier) {
  // multiplier -1 will scroll left, 1 will scroll right

  var photoWidth = 83;
  var scroll = photoWidth * multiplier;

  var scrollGoal = $('#photostrip').scrollLeft() + scroll;
  $('#photostrip').animate({scrollLeft: scrollGoal}, 200);
}

function setupScroll() {
  $('#scroll-left').click(function() {scrollStrip(-1);});
  $('#scroll-right').click(function() {scrollStrip(1);});
}
jQuery(setupScroll());

//$(document).ready(setupGallery());

/* navigation */
function prevPhoto() {
  var current = $('div.photo:visible')[0];
  console.info(current);
  var prev = $('div.photo + #' + current.id);
  console.info(prev);
  $(current).hide();
  $(prev).show();

  //var parent = ($(this).parent('div.photo'))[0];
  //$(parent).hide();
  //$("div.photo + #" + parent.id).show();
}

function nextPhoto() {
  var current = $('div.photo:visible')[0];
  var next = $('#' + current.id + ' + div.photo');
  $(current).hide();
  $(next).show();
}

function setupLinks() {
  $('#aboutlink').click(function() {
    $('#intro').hide();
    $('#about').show();
  });

  var images = $('div.photo img', $('#photobox'));
  images.each( function(i) {
    $(this).click(nextPhoto);
  });

  $('#photo-prev').click(function() {prevPhoto();});
  $('#photo-next').click(function() {nextPhoto();});

}


jQuery(setupLinks());
