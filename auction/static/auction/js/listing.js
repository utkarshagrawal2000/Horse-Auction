$(document).ready(function() {
    $('.list-group-item[data-toggle="collapse"]').click(function() {
      var icon = $(this).find('.collapse-icon i');
      icon.toggleClass('fas fa-plus fas fa-minus'); // Toggle plus/minus icons
    });
  });


