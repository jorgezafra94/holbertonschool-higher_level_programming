$(function () {
  $('INPUT#btn_translate').click(function () {
    const idioma = $('INPUT#language_code').val();
    $.get('https://www.fourtonfish.com/hellosalut/', { lang: idioma }, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
  $('INPUT#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      $('INPUT#btn_translate').click();
    }
  });
});
