const clearMembers = ["INPUT", "TEXTAREA"]

window.addEventListener("DOMContentLoaded", _ => {
  var clearBtns = getElms('form button[clear]')
  for(var clearBtn of clearBtns) {
    clearBtn.addEventListener("click", e => {
      for(var formMember of e.currentTarget.form) {
        if (clearMembers.includes(formMember.tagName)) {
          formMember.value = ""
        }
      }
    })
  }
})