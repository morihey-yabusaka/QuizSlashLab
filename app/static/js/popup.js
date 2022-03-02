window.addEventListener("DOMContentLoaded", _ => {
  var popupElms = getElms(".popup")
  for(var popupElm of popupElms) {
    var popupTriger = popupElm.querySelector(".click")
    popupTriger.addEventListener("click", e => {
      e.currentTarget.parentElement.classList.toggle("on")
    })
  }
})