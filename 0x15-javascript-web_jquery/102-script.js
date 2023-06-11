$('document').ready(function () {
    $('INPUT#btn_translate').click(function () {
        $.get('https://www.fourtonfish.com/hellosalut/hello/' + $.param($('INPUT#language_code').vall()), function (data) {
            $('DIV#hello').text('salut');
        });
    });
});