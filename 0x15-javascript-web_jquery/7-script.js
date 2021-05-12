const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

$.getJSON(url, function (variable) {
  $('DIV#character').text(variable.name);
});
