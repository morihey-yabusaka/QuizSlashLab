function createSNSURL(sns, url, text) {
  url = encodeURIComponent(decodeURIComponent(url))
  text = encodeURIComponent(decodeURIComponent(text))
  var apiUrl = ""

  if("twitter" == sns) {
    apiUrl = "https://twitter.com/share?text=" + text + "&url=" + url
  } else if ("line" == sns) {
    apiUrl = "http://line.me/R/msg/text/?" + text + "%20" + url
  } else {
    throw new Error("unknown sns value")
  }
  return apiUrl
}