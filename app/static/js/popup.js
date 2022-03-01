window.addEventListener("DOMContentLoaded", _ => {
  var popupElms = getElms(".popup")
  for(var popupElm of popupElms) {
    console.log(popupElm)
    var popupTriger = popupElm.querySelector(".click")
    console.log(popupTriger)
    popupTriger.addEventListener("click", e => {
      popupElm.classList.toggle("on")
    })
  }
})