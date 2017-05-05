function logout() {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open('POST', "/logout/", true)
    xmlhttp.send()
}