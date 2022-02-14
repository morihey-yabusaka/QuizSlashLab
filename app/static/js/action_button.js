function action_button(elm, type, username, pk) {
  url = ''
  if (type == "gq") {
    url = good_quiz_url.replace("123456789", pk).replace("username", username)
  } else if (type == "betamon") {
    url = betamon_url.replace("123456789", pk).replace("username", username)
  }
  $.ajax({
    type: 'POST',
    url: url,
    data: 'csrfmiddlewaretoken=' + csrftoken,
    success: (res) => {
      elm.classList.toggle("on")
      var cntELm = elm.querySelector(".cnt")
      var cnt = parseInt(cntELm.innerText)

      if(elm.classList.contains("on")) {
        cnt += 1
      } else {
        cnt -= 1
      }

      cntELm.innerText = cnt
    }
  })
}