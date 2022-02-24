function copy2clipboard(text, type) {
  if(navigator.clipboard) {
    navigator.clipboard.writeText(text).then(() => {
      notice(
        ["copy", type],
        "<span class='material-icons-outlined'>content_copy</span>コピーしました。"
      )
    })
  } else {
    alert('お使いのブラウザは対応していません')
  }
}

window.addEventListener('DOMContentLoaded', (e) => {
  var copyBtns = getElms(".btn-copy")
  for(var btn of copyBtns) {
    btn.addEventListener('click', (event) => {
      var text = event.currentTarget.getAttribute("data-text")
      var type = event.currentTarget.id
      copy2clipboard(text, type)
    })
  }
})