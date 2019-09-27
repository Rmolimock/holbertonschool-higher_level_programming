$(function () {
  $.get('https://swapi.co/api/films/?format=json', (data, textStatus) => {
    data.results.forEach((result) => {
      $('ul#list_movies').append('<li>' + result.title + '</li>');
    });
  });
});
