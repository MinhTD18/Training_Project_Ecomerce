

function checkRequire(){
   if(document.getElementById("user").value == "" 
   || document.getElementById("pass").value == ""
   || document.getElementById("confirm_pass").value == ""
   || document.getElementById("email").value == "" ){
       document.getElementById("mess")
       .innerText="Missing requirement fields!";
       return false;
   }
   return true;

}
function login(){
    if(checkRequire()){
       window.location.href="./main.html";
    }
}
