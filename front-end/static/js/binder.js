$("#search").keyup($.debounce(250, (event) => {
  genie.updatePage(0)
  genie.updateTotalPages(0)
  genie.fetch()
}))

$(".fa-sort").click((event) => {
  let state = (parseInt($(event.target).attr("state")) + 1) % 3
  $(".fa-sort").attr("state", 0)
  $(event.target).attr("state", state)
  genie.fetch()
})

$(".fa-step-forward").click((event) => {
  if (!$(event.target).hasClass("disabled")) {
    let newPage = genie.getPage() + 1
    genie.updatePage(newPage)
    genie.fetch()
  }
})

$(".fa-step-backward").click((event) => {
  if (!$(event.target).hasClass("disabled")) {
    let newPage = genie.getPage() - 1
    genie.updatePage(newPage)
    genie.fetch()
  }
})

$("#table tbody").on("click", "tr", (event) => {
  genie.show(event.currentTarget.id)
})
genie.fetch()
