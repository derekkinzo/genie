genie.plot = (data, id) => {
  $("#articles1h").text(data.gene_name + " Articles")
  $("#articles1").empty()

  let layout = {
    plot_bgcolor: "#222222",
    paper_bgcolor:"#222222",
    font: {
      color: 'white',
    },
    xaxis: {
      title: {
        text: 'Year',
        font: {
          family: 'Courier New, monospace',
          size: 18,
          color: '#7f7f7f'
        }
      }
    },
  }

  let traces = [
    {type: "scatter", mode: "lines", name: "publications", x: data.gene_data[0], y: data.gene_data[1]},
    {type: "scatter", mode: "lines", name: "citations", x: data.gene_data[0], y: data.gene_data[2]}
  ]
  Plotly.newPlot("histo1", traces, layout)

  $("#articles2h").text(data.disease_name + " Articles")
  $("#articles2").empty()
  // $.get({
  //   url: "/search?q=" + data[1],
  //   success: (data) => {
  //     for (let i = 0; i < data.length; i++) {
  //       let adiv = $("<div>")
  //       let atag = $("<a>" + data[i][0] + "</a>")
  //       atag.attr("href", data[i][1])
  //       adiv.append(atag)
  //       $("#articles2").append(adiv)
  //     }
  //   }
  // })

  // debugger
  // let layout = {
  //   title: {
  //     text: "Gene Disease Relationship Time Series",
  //   },
  //   plot_bgcolor: "#333333",
  //   paper_bgcolor:"#333333",
  //   font: {
  //     family: 'Arial, sans-serif',
  //     color: 'white',
  //   },
  //   xaxis: {
  //     title: {
  //       text: 'Day'
  //     }
  //   },
  //   yaxis: {
  //     title: {
  //       text: 'Occurances'
  //     }
  //   }
  // }
  //
  // $("#scatter").empty()
  // Plotly.newPlot("scatter", [{x: data.x, y: data.y, name: "Gene Disease", type: "scatter"}], layout)
}
