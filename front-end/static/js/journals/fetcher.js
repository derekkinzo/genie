journals.fetch = $.debounce(500, () => {
  let params = {search: $("#search").val()}

  let sort = $(".fa-sort[state=1]")[0] || $(".fa-sort[state=2]")[0]
  if (sort) {
    params.sortcol = $(sort).attr("col")
    params.sortstate = $(sort).attr("state")
  }

  params.page = journals.getPage()

  $.get("/journals", params, (data) => {
    journals.update(data)
  })
})

journals.getPage = () => {
  return parseInt($("#current-page").attr("page"))
}
