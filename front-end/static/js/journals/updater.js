journals.updater = {}
journals.updater.updater = (data) => {
  let table = $("#table")
  let tbody = table.find("tbody")
  tbody.empty()

  for (let i = 0; i < data.length; i++) {
    let tr = $("<tr>")
    let row = data[i]
    for (let j = 0; j < row.length; j++) {
      let td = $("<td>")
      let div = $("<div>" + row[j] + "</div>")
      td.append(div)
      tr.append(td)
    }
    tbody.append(tr)
  }
}

data = journals.fetcher.fetch(journals.updater.updater)
