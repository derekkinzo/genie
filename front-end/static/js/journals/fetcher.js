journals.fetch = () => {
  let params = {search: $("#search").val()}

  let sort = $(".fa-sort[state=1]")[0] || $(".fa-sort[state=2]")[0]
  if (sort) {
    params.sortcol = $(sort).attr("col")
    params.sortstate = $(sort).attr("state")
  }

  $.get("/journals", params, (data) => {
    journals.update(data)
  })
}
