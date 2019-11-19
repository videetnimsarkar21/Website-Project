
$(document).ready(function() {
    $('.tabing a').click(function (e) {
		e.stopPropagation();
		e.preventDefault();
		var tabcont = $(this).attr('href');
		$('.tabing a').removeClass('active');
		$(this).addClass('active');
		$('.tab1').fadeOut(0);
		$(tabcont).fadeIn(200); 
    });
	$('.tab-content .triptype label').click(function(){
		$(this).addClass('active');
		$(this).siblings().removeClass('active');
	});
	$('.tab-content .triptype label.oneTrip ').click(function(){
		$('.hide_one-trip').hide();
	});
	$('.tab-content .triptype label.rndTrip ').click(function(){
		$('.hide_one-trip').show();
	});
	 	
});

$( function() {
    $( "#depart" ).datepicker({
      numberOfMonths: 2,
      showButtonPanel: true
	
    });
} );



<script>  
var num = 0
$(".num").val(num);
$(".plus").click(function(){
  num = num + 1;
  if (num >10) {
   num = 10
$(this).parents(".col-xs-4").find(".message").val("Maximum Limit");
}
else {
$(this).parents(".col-xs-4").find(".message").val("");
}
                $(this).next(".num").val(num);
});
$(".minus").click(function(){
  num = num - 1;
   if (num < 0) {
    num = 0
                $(this).parents(".col-xs-4").find(".message").val("Minimum Limit");
}
else {
$(this).parents(".col-xs-4").find(".message").val("");
}
  $(this).prev(".num").val(num);
});
