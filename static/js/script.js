current_file = "";

$('.files').click(function() {
  f1 = $(this).html();
  current_file = f1;
  $('#cleanerForm #dfile1').val(f1);
  $("#working_file").text(f1);
  // console.log(f1);
  $.post("/file-data?string="+f1,
    //    {
    //        string:f1
    //    },
       function(result){
        $('#sheetnameid').val(result.data)
       }
       );
});
