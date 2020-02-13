$(function () {
  $.get('https://swapi.co/api/films/?format=json', function (data) {
    const lista = data.results;
    for (const elem of Object.values(lista)) {
      $('UL#list_movies').append('<li>' + elem.title + '</li>');
    }
  });
});
