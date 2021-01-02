

function checkRequire(){
   if(document.getElementById("user").value == "" 
   || document.getElementById("pass").value == "" ){
       document.getElementById("mess")
       .innerText="Bạn cần nhập đủ username và password.";
       return false;
   }
   return true;
}
function login(){
    if(checkRequire()){
       window.location.href="./main.html";
    }
}
