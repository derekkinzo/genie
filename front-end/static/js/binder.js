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
  $("#table tbody tr").removeClass("selected")
  $(event.currentTarget).addClass("selected")
  genie.show(event.currentTarget.id)
})

for (let i = 1; i <= 2; i++) {
  $("#gene-plot-select-" + i).click(() => {
    $("#gene-plot-select *").removeClass("selected")
    $("#gene-plot-select-" + i).addClass("selected")

    let layout = {
      plot_bgcolor: "#222222",
      paper_bgcolor:"#222222",
      font: {color: 'white'},
      hoverinfo: false,
      margin: {l: 40, r: 40, b: 40, t: 40, pad: 0}
    }

    let trace = [{type: "scatter", mode: "lines", x: genie.relationship.gene_data[0], y: genie.relationship.gene_data[i]}]
    Plotly.newPlot("gene-plot", trace, layout, {displayModeBar: false})
  })
}

for (let i = 1; i <= 2; i++) {
  $("#disease-plot-select-" + i).click(() => {
    $("#disease-plot-select *").removeClass("selected")
    $("#disease-plot-select-" + i).addClass("selected")

    let layout = {
      plot_bgcolor: "#222222",
      paper_bgcolor:"#222222",
      font: {color: 'white'},
      margin: {l: 40, r: 40, b: 40, t: 20, pad: 0}
    }

    let trace = [{type: "scatter", mode: "lines", x: genie.relationship.disease_data[0], y: genie.relationship.disease_data[i]}]
    Plotly.newPlot("disease-plot", trace, layout, {displayModeBar: false})
  })
}

$("#stats").on("click", ".stat-select", (event) => {
  $("#stats .stat-select").removeClass("selected")
  $(event.target).addClass("selected")
  let type = $(event.target).text()

  let layout = {
    plot_bgcolor: "#222222",
    paper_bgcolor:"#222222",
    font: {color: 'white'},
    margin: {l: 40, r: 40, b: 40, t: 20, pad: 0}
  }

  let trace = [{type: "scatter", mode: "lines", x: genie.relationship.stats[type][0], y: genie.relationship.stats[type][1]}]
  Plotly.newPlot("stats-plot", trace, layout, {displayModeBar: false})
})

genie.fetch()
