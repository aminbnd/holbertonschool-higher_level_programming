const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.getJSON(url, function (variable) {
  $.each(variable.results, function (i, movie_title) {
    $('UL#list_movies').append('<li>' + movie_title.title + '</li>');
  });
});
