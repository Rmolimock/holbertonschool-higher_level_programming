$(function () {
  $.get('https://swapi.co/api/people/5/?format=json', (data, textStatus) => {
    $('DIV#character').text(data.name);
  });
});
