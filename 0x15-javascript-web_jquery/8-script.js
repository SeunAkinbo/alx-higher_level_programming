/* The script that fetches and lists the title for all movies
   by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json

   All movie titles must be list in the HTML tag UL#list_movies
   Use of document.querySelector is prohibitted
   JQuery API is mandatory
*/

$(document).ready(function () {
  $.get(
    "https://swapi-api.alx-tools.com/api/films/?format=json",
    function (data) {
      for (const movie of data.results) {
        $("UL#list_movies").append("<li>" + movie.title + "</li>");
      }
    }
  );
});
