journals.fetcher = {}
journals.fetcher.fetch = (updater) => {
  $.get("/journals", (data) => {
    updater(data)
  })
}
