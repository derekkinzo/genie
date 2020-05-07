genie.select = (data) => {
  genie.relationship = data
  $("#gene-plot-select-1").trigger("click")
  $("#disease-plot-select-1").trigger("click")

  $("#gene-name").text(data.gene_name)
  $("#disease-name").text(data.disease_name)

  genie.updateLinks($("#gene-articles"), data.gene_links)
  genie.updateLinks($("#disease-articles"), data.disease_links)

  $("#stats").empty()

  for (let i = 0; i < data.stats.length; i++) {
    let select = $("<div>" + data.stats[i][0] + "</div>")
    select.addClass("tab-select")
    $(select).attr("index", i)
    $("#stats").append(select)
  }

  $("#stats").find(".tab-select").first().trigger("click")
}

genie.updateLinks = ($el, data) => {
  $el.empty()
  for (let i = 0; i < data.length; i++) {
    let lidiv = $("<li>")
    lidiv.addClass("article-link")

    let atag = $("<a>" + data[i][0] + ", page rank: " + data[i][3] + ", citations: " + data[i][2] + "</a>")
    atag.attr("target", "_blank")
    atag.attr("href", data[i][1])
    lidiv.append(atag)
    $el.append(lidiv)
  }
}
