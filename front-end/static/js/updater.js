genie.update = (data) => {
  let table = $("#table")
  let tbody = table.find("tbody")
  tbody.empty()

  for (let i = 0; i < data.items.length; i++) {
    let tr = $("<tr>")
    let row = data.items[i]
    tr.attr("id", row[0])
    for (let j = 0; j < row.length; j++) {
      let td = $("<td>")
      let div = $("<div>" + row[j] + "</div>")
      td.append(div)
      tr.append(td)
    }
    tbody.append(tr)
  }
  $($(tbody).find("tr")[0]).trigger("click")

  genie.updateTotalPages(data.total_pages)
  $(".fa-step-backward").removeClass("disabled")
  if (genie.getPage() - 1 < 0)
    $(".fa-step-backward").addClass("disabled")
  $(".fa-step-forward").removeClass("disabled")
  if (genie.getPage() + 1 >= data.total_pages)
    $(".fa-step-forward").addClass("disabled")

  let a = document.getElementById("export")
  a.getElementsByTagName("span")[0].innerText = data.items.length
}

genie.updatePage = (page) => {
  $("#current-page").attr("page", page)
  $("#current-page").text(page + 1)
}

genie.updateTotalPages = (total) => {
  $("#total-pages").text(total)
}
