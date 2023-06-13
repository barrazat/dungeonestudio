$(document).ready(function(){
    // Add smooth scrolling to all links
    $("a").on('click', function(event) {
  
      // Make sure this.hash has a value before overriding default behavior
      if (this.hash !== "") {
        // Prevent default anchor click behavior
        event.preventDefault();
  
        // Store hash
        var hash = this.hash;
  
        // Using jQuery's animate() method to add smooth page scroll
        // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
        $('html, body').animate({
          scrollTop: $(hash).offset().top
        }, 650, function(){
  
          // Add hash (#) to URL when done scrolling (default click behavior)
          window.location.hash = hash;
        });
      } // End if
    });
  });

let menu = document.getElementById("menu")
let header = document.getElementById("header")
let nav = document.getElementById("nav")

function ajustarTamañoHeader(){
    header.style.height = "50px"
}

menu.addEventListener("click", function(){
    if(header.style.height == "50px" || header.offsetHeight == 50) {
        header.style.height = "100%";
    } else {
        ajustarTamañoHeader();
    }
    
})

document.getElementById("home").onclick = function(){
    if(header.style.height == "100%"){
        ajustarTamañoHeader();
    }
}

document.getElementById("bio").onclick = function(){
    if(header.style.height == "100%"){
        ajustarTamañoHeader();
    }
}

document.getElementById("references").onclick = function(){
    if(header.style.height == "100%"){
        ajustarTamañoHeader();
    }
}

document.getElementById("prices").onclick = function(){
    if(header.style.height == "100%"){
        ajustarTamañoHeader();
    }
}

window.addEventListener("resize", function(){
    let ancho = document.documentElement.clientWidth

    if(ancho > 480) {
        header.style = ""
    }
})