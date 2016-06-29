 $(document).ready(function() {
    $('input#emailcol, input#phonecol').characterCounter();

        // hidding and unhidding fileds according to checked checkboxes
    $('input#phonecol').hide();
    $("input#test5").click(function(event) {
    if ($('input#test5').is(":checked"))
      $("input#phonecol").show();
    else
      $("#phonecol").hide();
  });

    $('input#emailcol').hide();
    $("input#test6").click(function(event) {
    if ($('input#test6').is(":checked"))
      $("input#emailcol").show();
    else
      $("#emailcol").hide();
  });


    $('input#dfile2').hide();
    $("input#compare").click(function(event) {
    if ($('input#compare').is(":checked"))
      $("input#dfile2").show();
    else
      $("#dfile2").hide();
  });


    // Form Validation
 



});
