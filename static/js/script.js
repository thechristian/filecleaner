$('#test').click(function() {
  $.getJSON('http://127.0.0.1:5000/files', function(data) {
    for (var i = data['files'].length - 1; i >= 0; i--) {
      console.log(data['files'][i]);
    }
  });
});

$('.files').click(function() {
  $('#cleanerForm #dfile1').val($(this).html());
});