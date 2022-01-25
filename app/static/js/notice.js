function createNoticeItem(class_, message, liveTime=5) {
  var elm = newElm("notice_item")
  if(Array.isArray(class_)) {
    elm.classList.add(...class_)
  } else {
    elm.classList.add(class_)
  }
  elm.innerHTML = message
  elm.setAttribute("data-live-time", liveTime)
  return elm
}

function onNoticeItem(noticeItemElm) {
  noticeItemElm.classList.add("on")
  var liveTime = noticeItemElm.getAttribute("data-live-time")
  noticeItemElm.addEventListener("animationend", e => {
    if(noticeItemElm.classList.contains("off")) {
      noticeItemElm.remove()
    }
  })
  setTimeout(_ => {
    noticeItemElm.classList.remove("on")
    noticeItemElm.classList.add("off")
  }, parseInt(liveTime) * 1000)
}

var listELm
window.addEventListener("DOMContentLoaded", _ => {
  listELm = getElm(".notice_list")
})

function notice(class_, message, liveTime=5) {
  var elm = createNoticeItem(class_, message, liveTime)
  listELm.appendChild(elm)
  onNoticeItem(elm)
}