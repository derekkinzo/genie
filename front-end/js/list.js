$("#search").keyup((event) => {
  updateData()
})

$("#table .fa-sort").click((event) => {
  let state = (parseInt(event.target.getAttribute("state")) + 1) % 3
  event.target.setAttribute("state", state)
  for (let j = 0; j < numColumns; j++) {
    if ($("#table thead tr .fa-sort")[j] != event.target) {
      $("#table thead tr .fa-sort")[j].setAttribute("state", 0)
    }
  }
  updateData()
})

function updateData() {
  let value = $("#search").val().toLowerCase()
  currentData = []
  for (let i = 0; i < genieData.length; i++) {
    for (let j = 0; j < numColumns; j++) {
      if (genieData[i][j].toString().toLowerCase().includes(value)) {
        currentData.push(genieData[i])
        break
      }
    }
  }

  for (let j = 0; j < numColumns; j++) {
    let state = $("#table thead tr .fa-sort")[j].getAttribute("state")
    let factor = 0
    if (state == "1") {
      currentData.sort((a, b) => {
        if (a[j] > b[j]) {
          return -1
        } else if (a[j] < b[j]) {
          return 1
        } else {
          return 0
        }
      })
    } else if (state == "2") {
      currentData.sort((a, b) => {
        if (a[j] > b[j]) {
          return 1
        } else if (a[j] < b[j]) {
          return -1
        } else {
          return 0
        }
      })
    }
  }
  updateTable(currentData)
}

function updateTable(data) {
  let table = $("#table")
  let tbody = table.find("tbody")
  tbody.empty()

  for (let i = 0; i < data.length; i++) {
    let tr = $("<tr>")
    let row = data[i]
    for (let j = 0; j < numColumns; j++) {
      let td = $("<td>")
      let div = $("<div>" + row[j] + "</div>")
      td.append(div)
      tr.append(td)
    }
    tr.click((event) => {
      updateQuad(data[i], i)
    })
    tbody.append(tr)
  }

  updateQuad(data[0], 0)

  let csv = ""
  data.forEach(function (row) {
    csv += row.join(",")
    csv += "\n"
  })
  let a = document.getElementById("export")
  a.getElementsByTagName("span")[0].innerText = data.length
  a.href = "data:text/csv;charset=utf-8," + encodeURI(csv)
  a.download = "data.csv"
}

function updateQuad(data, index) {
  $("#table tbody tr").removeClass("selected")
  $("#table tbody tr")[index].classList.add("selected")
  $("#histo1").empty()
  Plotly.newPlot("histo1", [{x: data[numColumns + 1], y: data[numColumns + 2], type: "bar"}], {
    title: {
      text: "Gene Distribution"
    },
    plot_bgcolor: "#222222",
    paper_bgcolor:"#222222",
    xaxis: {
      title: {
        text: 'Year'
      },
    },
    yaxis: {
      title: {
        text: 'Number of Publications'
      },
    },
    font: {
      family: 'Arial, sans-serif',
      color: 'white',
    },
  })

  $("#histo2").empty()
  Plotly.newPlot("histo2", [{x: data[numColumns + 3], y: data[numColumns + 4], type: "bar"}], {
    title: {
      text: "Disease Distribution"
    },
    plot_bgcolor: "#222222",
    paper_bgcolor:"#222222",
    xaxis: {
      title: {
        text: 'Year'
      }
    },
    yaxis: {
      title: {
        text: 'Number of Publications'
      }
    },
    font: {
      family: 'Arial, sans-serif',
      color: 'white',
    },
  })

  let layout = {
    title: {
      text: "Gene Disease Relationship Time Series",
    },
    plot_bgcolor: "#333333",
    paper_bgcolor:"#333333",
    font: {
      family: 'Arial, sans-serif',
      color: 'white',
    },
    xaxis: {
      title: {
        text: 'Day'
      }
    },
    yaxis: {
      title: {
        text: 'Occurances'
      }
    }
  }
  $("#scatter").empty()
  Plotly.newPlot("scatter", [{x: data[numColumns + 5], y: data[numColumns + 6], name: "Disease", type: "scatter"}], layout)

  $("#articles1h").text(data[0] + " Articles")
  $("#articles1").empty()
  $.get({
    url: "/search?q=" + data[0],
    success: (data) => {
      for (let i = 0; i < data.length; i++) {
        let adiv = $("<div>")
        let atag = $("<a>" + data[i][0] + "</a>")
        atag.attr("href", data[i][1])
        adiv.append(atag)
        $("#articles1").append(adiv)
      }
    }
  })

  $("#articles2h").text(data[1] + " Articles")
  $("#articles2").empty()
  $.get({
    url: "/search?q=" + data[1],
    success: (data) => {
      for (let i = 0; i < data.length; i++) {
        let adiv = $("<div>")
        let atag = $("<a>" + data[i][0] + "</a>")
        atag.attr("href", data[i][1])
        adiv.append(atag)
        $("#articles2").append(adiv)
      }
    }
  })
}

updateData(genieData)
