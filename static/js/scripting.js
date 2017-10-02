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
  // add filesize method. this relies on the additional-methods script included
  $.validator.addMethod('filesize', function(val, field, flsize){
	  return this.optional(field) || (field.files[0].size <= flsize);
  });
  // Form Validation
  $("#cleanerForm").validate({
    rules: {
      dataFile1: {
    	  required: true, 
    	  extension: "xlsx|xls|csv",
    	  filesize:3000000
      },
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
        required: "#compare:checked",
        filesize:3000000
      },
    },
    messages: {
      dataFile1: "Upload a < 3MB xls/xlsx/csv file",
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
