 $(document).ready(function() {
// move init code from materialize here
  $('.button-collapse').sideNav();

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

  $("#cleanerForm").validate({
    rules: {
      dataFile1: "required",
      phonenumbercol: {
        required: "#test5:checked",
        minlength: 20
      },
      emailcol: {
        required: "#test6:checked",
        maxlength: 20
      },
      dataFile2: {
        required: "#compare:checked"
      },
      
    },
    messages: {
      dataFile1: "Please this file is required.",
      phonenumbercol: {
        required: "This field is needed",
        maxlength: "Enter atmost 20 characters for the column name."
      },
      emailcol: {
        required: "This field is needed.",
        minlength: "Enter atmost 20 characters for the column name."
      },
      dataFile2: {
        required: "Please upload a second file to compare with."
      },
    }
  });

  // $('#isubmit').click(function(){
  // 	//check whether browser fully supports all File API
  // 	if (window.File && window.FileReader && window.FileList && window.Blob){
  // 		//get the file size and file type from file input field
  // 		var fsize = $('#dfile1')[0].files[0].size;
  //       var ftype = $('#dfile1')[0].files[0].type;
  //       var fname = $('#dfile1')[0].files[0].name;

  //       if (fsize>3048576) {
  //       	alert("Type :"+ ftype +" | "+ fsize +" bites\n(File: "+fname+") Too big!");
  //       }
  //       else {
  //       	con
  //       }
  // 	}
  // 	else{
  // 		alert("Please upgrade your browser, because your current browser lacks some new features we need!");
  // 	}
  // });

});
