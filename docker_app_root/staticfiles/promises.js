function _listeners(){
  if (document.readyState === 'complete' || document.readyState === 'interactive'){
    // Promise 1 - get encoding/decoding flask session from celery worker 
    $('#btn-submit-promise').on('click', function() {
      $.ajax({
        url: 'celery/tasks/f_query_01/',
        data: { secret_key: $('#id_secret_key').attr('value'),
                cookie_value: $('#id_cookie_value').text(),
                operation: $('#id_operation option:selected').text()},
        method: 'POST',
      }).done( (res) => {
        getStatus(res.task_id);
      }).fail( (err) => {
        console.log(err);
      })
    });
  }
  else{
    setTimeout(_listeners, 1);
  }
}

function getStatus(taskid){
  a = $.ajax({
    url: `getstatus/${taskid}`,
    method: 'POST'
  })
  .done( (res) => { 
    $("#id-returned-data").html(
      `<p class="data-id-01" id="data-id-01"> id: ${res.task_id} </p>
       <p class="data-status-01" id="data-status-01"> status: ${res.task_status} </p>
       <p class="data-result-01" id="data-result-01"> result: ${res.task_result} </p>`
      );
    // window['debugged'] = res;
  }
   );
}


_listeners()