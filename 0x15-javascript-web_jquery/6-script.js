/* script that updates the text of the <header> element
   to New Header!!! when the user clicks on DIV#update_header

   Use of document.querySelector is prohibitted
   JQuery API is mandatory
*/
$(document).ready(function () {
  $("DIV#update_header").click(function () {
    $("header").text("New Header!!!");
  });
});
