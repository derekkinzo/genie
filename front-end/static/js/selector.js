genie.select = (data) => {
  genie.relationship = data
  $("#gene-plot-select-1").trigger("click")
  $("#disease-plot-select-1").trigger("click")

  $("#gene-name").text(data.gene_name)
  $("#disease-name").text(data.disease_name)

  $.get({
    url: "/search?q=" + data.gene_name,
    success: (data) => {
      genie.updateLinks($("#gene-articles"), data)
    }
  })

  $.get({
    url: "/search?q=" + data.disease_name,
    success: (data) => {
      genie.updateLinks($("#disease-articles"), data)
    }
  })
}

genie.updateLinks = ($el, data) => {
  $el.empty()
  for (let i = 0; i < data.length; i++) {
    let adiv = $("<div>")
    adiv.addClass("article-link")

    let atag = $("<a>" + data[i][0] + "</a>")
    atag.attr("target", "_blank")
    atag.attr("href", data[i][1])
    adiv.append(atag)
    $el.append(adiv)
  }
}
