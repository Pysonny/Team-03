const star = document.querySelector('#star-check');
const rating = document.querySelector('#rating')

$(document).ready(function() {
  // Define variables to store the percentage values
  var left = 0;
  var right = 0;
  var isclick = 0;
  var clicked = 0;
  
  // Add click event to the SVG tags
  $('.clickable-star').on('click', function(event) {
    // Get the current SVG tag's ID
    var id = $(this).attr('id');
    var x = event.pageX - $(this).offset().left;
    console.log(x);
    isclick = 1;
    
    if (id == 'star-1') {
      left = 1;
      right = 2;
    } else if (id == 'star-2') {
      left = 3;
      right = 4;
    } else if (id == 'star-3') {
      left = 5;
      right = 6;
    } else if (id == 'star-4') {
      left = 7;
      right = 8;
    } else if (id == 'star-5') {
      left = 9;
      right = 10;
    }

    if (x < $(this).width() / 2) {
      star.classList.add(`star-check-${left}`);
      clicked = left;
      rating.setAttribute('value', `${left/2}`)
    } else {
      star.classList.add(`star-check-${right}`);
      clicked = right;
      rating.setAttribute('value', `${left/2}`)
    }
  });
  
  // Add mouseover event to the SVG tags
  $('.clickable-star').on('mouseover', function(event) {
    // Get the current mouse position relative to the SVG tag
    star.className = "";
    var id = $(this).attr('id');
    var x = event.pageX - $(this).offset().left;

    if (id == 'star-1') {
      left = 1;
      right = 2;
    } else if (id == 'star-2') {
      left = 3;
      right = 4;
    } else if (id == 'star-3') {
      left = 5;
      right = 6;
    } else if (id == 'star-4') {
      left = 7;
      right = 8;
    } else if (id == 'star-5') {
      left = 9;
      right = 10;
    }
    
    if (x < $(this).width() / 2) {
      star.classList.add(`star-check-${left}`);
    } else {
      star.classList.add(`star-check-${right}`);
    }
  });

  $('.clickable-star').on('mouseout', function(event) {
    star.className = "";
    if (isclick) {
      star.classList.add(`star-check-${clicked}`);
    } else {
      star.classList.add('star-check-0');
    }
  });
});
