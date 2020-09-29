function show()
 {
 var pass=document.getElementById('pword');

  if(document.getElementById('check').checked)
    {

    pass.setAttribute('type','text');
    }
   else{
    pass.setAttribute('type','password');
       }
 }