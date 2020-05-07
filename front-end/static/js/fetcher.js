genie.fetch = (format) => {
  let params = {search: $("#search").val()}

  let sort = $(".fa-sort[state=1]")[0] || $(".fa-sort[state=2]")[0]
  if (sort) {
    params.sortcolumn = $(sort).attr("column")
    params.sortstate = $(sort).attr("state")
  }

  params.page = genie.getPage()

  if (format == "csv") {
    params.format = format
    window.location = "/relationships?" + jQuery.param(params)
  } else {
    $('#loading-indicator').show()
    $.get("/relationships", params, (data) => {
      genie.update(data)
      $('#loading-indicator').hide()
    })
  }
}

genie.show = (id) => {
  $.get("/relationships/" + id, (data) => {
    genie.select(data)
  })
}

genie.getPage = () => {
  return parseInt($("#current-page").attr("page"))
}
