$(function () {
  $('#btn_translate').click(function () {
    const idioma = $('#language_code').val();
    $.get('https://www.fourtonfish.com/hellosalut/', { lang: idioma }, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
