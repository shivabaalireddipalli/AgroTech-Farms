function validpassword()
{
      var password=document.myform.pass1.value;
      var cpassword=document.myform.pass2.value;

           if(password.length<5)
           {
           alert("please enter atleast 5  characters");
           return false;
           }
                if(password==cpassword)
                {
                return true;
                }
                else
                {
				alert("password & confirm password must be same");
                return false;
                }


}
function patter()
{


}
