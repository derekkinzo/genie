journals.fetch = () => {
  let search = $("#search").val()

  $.get("/journals", {search: search}, (data) => {
    journals.update(data)
  })
}
