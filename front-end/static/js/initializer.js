$(document).ajaxStart(() => {
  $('#loading-indicator').show()
})

$(document).ajaxStop(() => {
  $('#loading-indicator').hide()
})
