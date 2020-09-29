function formvalidation()
{
 var num1 = document>getElementById("phone");
 if(isNaN(num1))
 {
	document.write(num1 + " is not a number <br/>");
 }
else
 {
	document.write(num1 + " is a number <br/>");
 }

}