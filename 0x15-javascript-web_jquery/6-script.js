/* Update header when div#update is clicked */
$(document).ready(function () {
  $("DIV#update_header").click(function () {
    $("header").text("New Header!!!");
  });
});
