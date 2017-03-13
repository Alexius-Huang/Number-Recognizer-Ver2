$(document).ready(function() {
  $('#feed-btn').on('click', function(event) {
    event.preventDefault();
    var canvas = document.getElementById('main-canvas');
    var mime = 'image/jpeg';
    var imgURL = canvas.toDataURL(mime);
    var answer;
    var inputOptions = new Promise(function (resolve) {
      setTimeout(function () {
        resolve({
          0: '0',
          1: '1',
          2: '2',
          3: '3',
          4: '4',
          5: '5',
          6: '6',
          7: '7',
          8: '8',
          9: '9',
        })
      }, 500)
    })
    swal({
      title: 'Select the Answer of the Image',
      background: '#66e3b2',
      showCancelButton: true,
      confirmButtonText: 'Submit',
      confirmButtonColor: '#23bf82',
      cancelButtonColor: '#db3a79',
      allowOutsideClick: false,
      allowEscapeKey: false,
      input: 'radio',
      inputOptions: inputOptions,
      inputValidator: function(result) {
        return new Promise(function (resolve, reject) {
          if (result) {
            answer = result;
            resolve();
          } else reject('You need to select an answer!');
        });
      }
    }).then(function(result) {
      swal({
        title: 'Processing ...',
        timer: 2000,
        showConfirmButton: false,
        background: '#23bf82'
      }).then(function() { /* DO NOTHING */ })
      /* Send AJAX POST */
      var token = $('input[name="csrfmiddlewaretoken"]').prop('value');
      $.ajax({
        type: 'post',
        url:  'feed/',
        data: { imgURL: imgURL, number: answer },
        dataType: 'json',
        cache: false,
        beforeSend: function(jqXHR, settings) { jqXHR.setRequestHeader('x-csrftoken', token); },
        success: function(data) {
          /* DO SOMETHING */
        }
      });
    });
  });

  $('#generate-btn').on('click', function(event) {
    /* Send AJAX POST */
    var token = $('input[name="csrfmiddlewaretoken"]').prop('value');
    $.ajax({
      type: 'post',
      data: { ajax: 'true' },
      dataType: 'json',
      url: 'generate_data/',
      cache: false,
      beforeSend: function(jqXHR, settings) { jqXHR.setRequestHeader('x-csrftoken', token); },
      success: function(data) {
        /* DO SOMETHING */
        console.log(data);
      }
    });
  });

  $('#learn-btn').on('click', function(event) {
    /* Send AJAX POST */
    $.ajax({
      type: 'post',
      url:  './learn'
    });
  });

});