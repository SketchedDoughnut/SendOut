window.addEventListener('load', function () {
    var infoCards = document.getElementById("img-holder")
if (window.innerWidth < 900) {
    infoCards.style.setProperty("--row-length", "2")
}
  })