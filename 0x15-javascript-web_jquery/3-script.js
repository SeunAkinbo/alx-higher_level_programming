/* The script updates the text color of the <header> element to
   red (#FF0000) when the user clicks on the tag DIV#red_header:
   Use of document.querySelector is not allowed
   You must use the JQuery API
*/

$(document).ready(() => {
  $("DIV#red_header").click(() => {
    $("header").addClass("red");
  });
});
