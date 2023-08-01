function sleep(ms = 0) {
  return new Promise(resolve => setTimeout(resolve, ms));
}
var myInput=false
//zdefiniowanie obiecktu input
var input = document.getElementById("input");
//czekanie aż w inpucie pojawi się enter
input.addEventListener("keypress", function(event) {
  if (event.key === "Enter") {
    event.preventDefault();
    //wysylanie danych do pythona
    eel.sendMessage(document.querySelector('input').value);
    //przewijanie
    myInput=true
    //resetowanie pola tekstowego
    document.querySelector('input').value="";
    
  };
});





// Onclick of the button
//document.querySelector("button").onclick = function () {  
    // Call python's random_python function
  //  eel.random_python()(function(number){                      
      // Update the div with a random number returned by python
    //  document.querySelector(".random_number").innerHTML = number;
   // })
 // }


//function myFunction() {
  //  document.querySelector(".random_number").innerHTML = "WOW";
 // }
//myFunction()//;
eel.getLastMessages()(function(messages){                      
  document.querySelector("#messages").innerHTML = messages;
  var objDiv = document.getElementById("scrool");
  objDiv.scrollTop = objDiv.scrollHeight;
})
eel.expose(getNewMessages)
function getNewMessages (messages){                      
  document.querySelector("#messages").innerHTML = messages;
  if (myInput==true){
    var objDiv = document.getElementById("scrool");
    objDiv.scrollTop = objDiv.scrollHeight;
    myInput=false;
  };

  
};