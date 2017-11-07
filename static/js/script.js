current_file = "";
current_file_data = "";

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
        console.log(result);
        current_file_data = result.data;
        // $('#sheetnameid').val(Object.keys(result.data));
        makeSelect(Object.keys(current_file_data),'#sheetnameid');
       }
       );
});

function makeSelect(opts,ID){
  var newOpts = "";
  for (var i = opts.length - 1; i >= 0; i--) {
    // create radio button for opts[i]
    newOpts += "<option value='"+opts[i]+"'>"+opts[i]+"</option>";
  }
  $(ID).html(newOpts).show();
}

function makeColumns(){
  sheet = $('#sheetnameid').val();
  opts = current_file_data[sheet];
  ID = '.sheetnameid_cols';
  makeSelect(opts,ID);
}