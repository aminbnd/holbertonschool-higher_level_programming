const url = 'https://fourtonfish.com/hellosalut/?lang=fr';

$(this).ready(function () {
  $.getJSON(url, function (greetingfr) {
    $('DIV#hello').text(greetingfr.hello);
  });
});
