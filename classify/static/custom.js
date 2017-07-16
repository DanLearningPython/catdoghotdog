$(document).ready( function() {
	$(document).on('change', '.btn-file :file', function() {
	var input = $(this),
		label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
	input.trigger('fileselect', [label]);
	});

	$('.btn-file :file').on('fileselect', function(event, label) {
	    
	    var input = $(this).parents('.input-group').find(':text'),
	        log = label;
	    
	    if( input.length ) {
	        input.val(log);
	    } else {
	        if( log ) alert(log);
	    }
    
	});
	function readURL(input) {
	    if (input.files && input.files[0]) {
	        var reader = new FileReader();
	        
	        reader.onload = function (e) {
	            $('#img-upload').attr('src', e.target.result);
	        }
	        
	        reader.readAsDataURL(input.files[0]);
	    }
	}
	$(document).ready(function (e) {
		$("#upload-image").on('submit',(function(e) {

			e.preventDefault();
			$(".panel").attr('class','panel panel-default');
			$("#message").empty();
			$('#loading').show();
			$.ajax({
				url: "/predict", // Url to which the request is send
				type: "POST",             // Type of request to be send, called as method
				data: new FormData(this), // Data sent to server, a set of key/value pairs (i.e. form fields and values)
				contentType: false,       // The content type used when sending data to the server.
				cache: false,             // To unable request pages to be cached
				processData:false, 
				dataType: 'json',     // To send DOMDocument or non processed data file it is set to false
				success: function(data)   // A function to be called if request succeeds
				{
					$('#loading').hide();
					$("."+data.label+" .panel-default").attr('class','panel panel-success');
					$("#dog").html(data.weights.dog);
					$("#cat").html(data.weights.cat);
					$("#hotdog").html(data.weights.hotdog);
				}
			});
		}));
	});	
	$("#imgInp").change(function(){
	    readURL(this);
	}); 	
});	