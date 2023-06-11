$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    for (item of data.results) {
        $('UL#list_movies').append(item.title).append("<br/>");
    }
});