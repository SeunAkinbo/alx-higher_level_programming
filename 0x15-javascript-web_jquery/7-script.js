/* The script that fetches the character name from this
URL: https://swapi-api.alx-tools.com/api/people/5/?format=json

   The name must be displayed in the HTML tag DIV#character
   Use of document.querySelector is prohibitted
   JQuery API is mandatory
*/

$(document).ready(function () {
  $.get(
    "https://swapi-api.alx-tools.com/api/people/5/?format=json",
    function (data) {
      $("DIV#character").text(data.name);
    }
  );
});
