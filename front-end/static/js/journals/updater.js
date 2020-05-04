journals.update = (data) => {
  let table = $("#table")
  let tbody = table.find("tbody")
  tbody.empty()

  for (let i = 0; i < data.items.length; i++) {
    let tr = $("<tr>")
    let row = data.items[i]
    for (let j = 0; j < row.length; j++) {
      let td = $("<td>")
      let div = $("<div>" + row[j] + "</div>")
      td.append(div)
      tr.append(td)
    }
    tbody.append(tr)
  }

  $("#total-pages").text(data.total_pages)
  $(".fa-step-backward").removeClass("disabled")
  if (journals.getPage() - 1 < 0)
    $(".fa-step-backward").addClass("disabled")
  $(".fa-step-forward").removeClass("disabled")
  if (journals.getPage() + 1 >= data.total_pages)
    $(".fa-step-forward").addClass("disabled")
}

journals.updatePage = (page) => {
  $("#current-page").attr("page", page)
  $("#current-page").text(page + 1)
}
