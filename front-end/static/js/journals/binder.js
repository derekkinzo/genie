$("#search").keyup($.debounce(500, (event) => {
  journals.updatePage(0)
  journals.fetch()
}))

$(".fa-sort").click((event) => {
  let state = (parseInt($(event.target).attr("state")) + 1) % 3
  $(".fa-sort").attr("state", 0)
  $(event.target).attr("state", state)
  journals.fetch()
})

$(".fa-step-forward").click((event) => {
  if (!$(event.target).hasClass("disabled")) {
    let newPage = journals.getPage() + 1
    journals.updatePage(newPage)
    journals.fetch()
  }
})

$(".fa-step-backward").click((event) => {
  if (!$(event.target).hasClass("disabled")) {
    let newPage = journals.getPage() - 1
    journals.updatePage(newPage)
    journals.fetch()
  }
})

journals.fetch()
