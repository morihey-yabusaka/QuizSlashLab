function action_button(elm, type, username, pk) {
  url = ''
  if (type == "gq") {
    url = good_quiz_url.replace("123456789", pk).replace("username", username)
  } else if (type == "betamon") {
    url = betamon_url.replace("123456789", pk).replace("username", username)
  }
  console.log(url);
  elm.classList.toggle("on")
  $.ajax({
    type: 'POST',
    url: url,
    data: 'csrfmiddlewaretoken=' + csrftoken,
    success: (res) => {
      console.log("success");
    }
  })
}