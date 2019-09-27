$(function () {
  $('DIV#update_header').click(() => {
    if ($('header').text() !== 'New Header!!!') {
      $('header').text('New Header!!!');
    } else {
      $('header').text('First HTML page');
    }
  });
});
