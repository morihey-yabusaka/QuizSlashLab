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

function setCssVar(elm, varName, value) {
  elm.style.setProperty(varName, value)
}
