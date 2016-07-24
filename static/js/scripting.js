 $(document).ready(function() {
// move init code from materialize here
  $('.button-collapse').sideNav();

  $('input#emailcol, input#phonecol').characterCounter();

      // hidding and unhidding fileds according to checked checkboxes
  $('input#dupcolid').hide();
  $("input#dupInCols").click(function(event) {
  if ($('input#dupInCols').is(":checked"))
    $("input#dupcolid").show();
  else
    $("#dupcolid").hide();
  });

  $('input#phonecol').hide();
  $("input#validatefonNum").click(function(event) {
  if ($('input#validatefonNum').is(":checked"))
    $("input#phonecol").show();
  else
    $("#phonecol").hide();
  });

  $('input#emailcol').hide();
  $("input#validateEmails").click(function(event) {
  if ($('input#validateEmails').is(":checked"))
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


  $("#cleanerForm").validate({
    rules: {
      dataFile1: "required",
      
      dupcolname: {
        required: "#dupInCols:checked",
        maxlength: 20
      },

      phonenumbercol: {
        required: "#validatefonNum:checked",
        maxlength: 20
      },
      emailcol: {
        required: "#validateEmails:checked",
        maxlength: 20
      },
      dataFile2: {
        required: "#compare:checked"
      },
      
    },
    messages: {
      dataFile1: "Please this file is required.",
      dupcolname: {
        required: "This field is needed",
        maxlength: "Enter atmost 20 characters for the column name"
      },
      phonenumbercol: {
        required: "This field is needed",
        maxlength: "Enter atmost 20 characters for the column name."
      },
      emailcol: {
        required: "This field is needed.",
        maxlength: "Enter atmost 20 characters for the column name."
      },
      dataFile2: {
        required: "Please upload a second file to compare with."
      },

    }
  });

});
