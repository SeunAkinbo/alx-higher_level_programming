/* The script that adds a <li> element to a list when the
   user clicks on the tag DIV#add_item.

   The new element must be: <li>Item</li>
   The new element must be added to UL.my_list

   Use of document.querySelector is prohibitted
   JQuery API is mandatory
*/
$(document).ready(function () {
  $("div#add_item").click(function () {
    $("ul.my_list").append("<li>Item</li>");
  });
});
