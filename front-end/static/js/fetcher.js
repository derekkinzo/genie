genie.fetch = () => {
  let params = {search: $("#search").val()}

  let sort = $(".fa-sort[state=1]")[0] || $(".fa-sort[state=2]")[0]
  if (sort) {
    params.sortcolumn = $(sort).attr("column")
    params.sortstate = $(sort).attr("state")
  }

  params.page = genie.getPage()

  $.get("/relationships", params, (data) => {
    genie.update(data)
  })
}

genie.show = (id) => {
  $.get("/relationships/" + id, (data) => {
    genie.plot(data)
  })
}

genie.getPage = () => {
  return parseInt($("#current-page").attr("page"))
}
