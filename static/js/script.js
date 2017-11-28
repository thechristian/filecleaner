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
        makeSelect(Object.keys(current_file_data),'#sheetnameid');
       }
       );
});

function makeSelect(opts,ID){
  var newOpts = "<option value=''>------</option>";
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

// $.post('/File-Cleaner', $('#cleanerForm').serialize())
function subForm() {
    var data = $('form').serialize();
    var url = "/File-Cleaner"; // the script where you handle the form input.
    $.post(url,data,
      function(resp){
        console.log(resp);
        res = resp.res;
        console.log(res);
        makeDownloads(res);
      }
    );
}

function makeDownloads(res){
  var temp = ``;
  $('#resultsHere').html('');

  if (res.row_dupes.status) {
    temp += `<div class="card-panel center-align hoverable">
                  <span class="blue-text text-darken-2"> Results for check duplicate in rows</span><br>
                  <a class="btn blue" href="/File-download?file=${res.row_dupes.result_path}">Download</a>
                </div>`;
  }

  if (res.col_dupes.status) {
    temp += `<div class="card-panel center-align hoverable">
                  <span class="blue-text text-darken-2">Results for check duplicates in column</span><br>
                  <a class="btn blue" href="/File-download?file=${res.col_dupes.result_path}">Download</a>
                </div>`;
  }

  if (res.col_email.status) {
    temp += `<div class="card-panel center-align hoverable">
                  <span class="blue-text text-darken-2">Results for validate email</span><br>
                  <a class="btn blue" href="/File-download?file=${res.col_email.result_path}">Download</a>
                </div>`;
  }

  $('#resultsHere').html(temp);
}

$(document).ready(function(){
  url = '/files-manager';
  $.get(url,
    function(resp){
      console.log(resp);
      
    }
  );
});
