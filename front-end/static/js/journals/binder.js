$("#search").keyup((event) => {
  journals.fetch()
})

$(".fa-sort").click((event) => {
  let state = (parseInt($(event.target).attr("state")) + 1) % 3
  $(".fa-sort").attr("state", 0)
  $(event.target).attr("state", state)
  journals.fetch()
})

journals.fetch()
