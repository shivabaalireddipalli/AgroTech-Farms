var gt = $j(".total");

$j(".quantity").change(function(){
    cal(this);
});
$j(".quantity").keyup(function(){
    cal(this);
});

function cal(quantityElem){

      var id = $j(quantityElem).data("id");
      var q = $j(quantityElem).value();
      var p = $j("#price"+id).text();

      $j("#total"+id).value(q*p);
      $j(".gtotal").html(gTotal());

}

function gTotal(){
    var t = 0;
   $j(".total").foreach(function(){
        if($j(this).value().length > 0)
         t += parseFloat($j(this).value(), 2);
   });

   return t.toFixed(2);
}