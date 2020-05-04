journals.plot = (data, id) => {
  $("#table tbody tr").removeClass("selected")
  $("#table tbody #" + id).addClass("selected")

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
  Plotly.newPlot("scatter", [{x: data.x, y: data.y, name: "Gene Disease", type: "scatter"}], layout)
}
