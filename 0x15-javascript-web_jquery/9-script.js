/* The script that fetches from 
   https://hellosalut.stefanbohacek.dev/?lang=fr and
   displays the value of hello from that fetch in the HTML tag DIV#hello.

   The translation of “hello” must be displayed in the HTML tag DIV#hello
   Use of document.querySelector is prohibitted
   JQuery API is mandatory
   Your script must work when it is imported from the <head> tag
*/

$(document).ready(function () {
  $.get("https://hellosalut.stefanbohacek.dev/?lang=fr", function (data) {
    $("DIV#hello").text(data.hello);
  });
});

