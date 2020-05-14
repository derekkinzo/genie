genie.fetch = (format) => {
  let params = {search: {}}

  $("#table thead th").each((index, th) => {
    let $input = $(th).find("input")
    let values = $input.map((index, input) => input.value).get()
    params.search[$input.attr("column")] = values.join(":")
  })

  let sort = $(".table-sort[state=1]")[0] || $(".table-sort[state=2]")[0]
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
