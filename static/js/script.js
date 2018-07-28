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
    $('#resultsHere').html("<img src='static/gif-load.gif' alt='Loading ...'><br><p>File is Preparing ...</p>");
    $.post(url,data,
      function(resp){
        // console.log(resp);
        res = resp.res;
        // console.log(res);
        makeDownloads(res);
      }
    );
}

function startUpload(){
     $('#cleanerForm .progress').show();;
    return true;
}

function stopUpload(status){
      if (status){
         initFileManager();
      }else {
         alert( "error" );
      }
      $('#cleanerForm .progress').hide();
      return true;
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

function fileManager(files){
  handle = `<ul class="collapsible z-depth-0" data-collapsible="expandable" style="max-height:400px;overflow:auto">`;
  handle += `<li><div class="collapsible-header" id="searchHead">
                <input id="search" type="text" class="validate" placeholder="search file"></div>
                <div id="searchResults" class="collapsible-body"></div></li>`;
  for (var item in files) {
    if (item == 'LEVEL') {
      continue;
    }else{
      handle += `<li>
                  <div class="collapsible-header" style="text-align:left" id="${item}"><i class="material-icons blue-text">folder</i>${item}</div>
                  <div class="collapsible-body"><div class="collection" style="text-align:left;">`;
      for (file of files[item]) {
        f1=item+"/"+file;
        f = file.split('.')
        file = f[f.length-2]
        handle += `<a href="#" data-file="${f1}" class="blue-text collection-item files" style="margin-left:40px">${file}</a>`;
      }
        handle += `</div></div></li>`;
    }
  }
  handle += '</ul>';
  return handle;
}

function search(files,search){
  results = `<div class="collection">`;
  for (var item in files) {
    if (item == 'LEVEL') {
      continue;
    }else{
      for (file of files[item]) {
        f1=item+"/"+file;
        f = file.split('.');
        file = f[f.length-2];
        re = new RegExp(search,'i');
        res = re.exec(file);
        if (res) {
          // results.push();
          results += `<a href="#" data-file="${f1}" class="blue-text collection-item files">${item+":"+file}</a>`;
        }
      }
    }
  }
  return results += `</div>`;
}

function initFileManager(){
  // requet files
  url = '/file-manager';
  $.get(url,
    function(resp){
      // console.log(resp);
      file_tree = resp.files;
      handle = fileManager(resp.files);

      $('#File-manager').empty().html(handle);
      // initialize collapsible
      $('.collapsible').collapsible();

      activateFiles();

    $("#search").keypress(function(e){
      if( e.which == 8 || e.which == 46 ){
          var valu = $(this).val();
        if (valu.length <= 2) {
          $("#searchResults").empty();
        }
      }else{
          var valu = $(this).val();
        if (valu.length > 1) {
          results = search(file_tree,valu);
          $("#searchResults").empty().html(results);
          expand("#searchHead");
          activateFiles();
        }
      }
    });
  });
}

function expand(that){
  $(".collapsible-header"+that).addClass("active");
  $(".collapsible").collapsible({accordion: false});
}

function collapse(that){
  $(".collapsible-header"+that).removeClass(function(){
    return "active";
  });
  $(".collapsible").collapsible({accordion: true});
  $(".collapsible").collapsible({accordion: false});
}

function activateFiles(){
  $('.files').click(function() {
    f1 = $(this).data('file');
    current_file = f1;
    $('#cleanerForm #dfile1').val(f1);
    // console.log(f1);
    $.get("/file-data?string="+f1,
      //    {
      //        string:f1
      //    },
     function(result){
      // console.log(result);
      current_file_data = result.data;
      makeSelect(Object.keys(current_file_data),'#sheetnameid');
    });
});
}

$(document).ready(function(){
    $('.dropdown-trigger').dropdown();
    $( document ).ajaxStart(function() {
      $('.btn').addClass('disabled');
    });
    $( document ).ajaxComplete(function() {
      $('.btn').removeClass('disabled');
    });
    current_file = "";
    current_file_data = "";
    file_tree = "";
    // $.get("/user-details",function(result){
    //   // console.log(result);
    // });
    initFileManager();
});
