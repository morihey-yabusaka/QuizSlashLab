// ex createElement
function newElm(className = undefined, tag = "div") {
  var elm = document.createElement(tag);
  if (className) elm.className = className;
  return elm;
}

// ex querySelector
function getElm(query) {
  return document.querySelector(query);
}
function getElms(query) {
  return document.querySelectorAll(query);
}

// ex css prop
function getCssVar(elm, varName) {
  return window.getComputedStyle(elm, null).getPropertyValue(varName);
}


function copy2clipboard(text) {
  if(navigator.clipboard) {
    navigator.clipboard.writeText(text).then(() => {
      alert('コピーしました')
    })
  } else {
    alert('お使いのブラウザは対応していません')
  }
}

window.addEventListener('load', (e) => {
  var copyBtns = getElms(".btn-copy")
  for(var btn of copyBtns) {
    btn.addEventListener('click', (event) => {
      copy2clipboard(event.currentTarget.getAttribute("data-text"))
    })
  }
})