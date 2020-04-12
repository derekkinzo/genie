headers = ["Gene", "Disease", "Metric"];
var dataSet = [
  ["5421", "2011/04/25", "$320,800"],
  ["8422", "2011/07/25", "$170,750"],
  ["1562", "2009/01/12", "$86,000"],
  ["6224", "2012/03/29", "$433,060"],
  ["5407", "2008/11/28", "$162,700"],
  ["4804", "2012/12/02", "$372,000"],
  ["9608", "2012/08/06", "$137,500"],
  ["6200", "2010/10/14", "$327,900"],
  ["2360", "2009/09/15", "$205,500"],
  ["1667", "2008/12/13", "$103,600"],
  ["3814", "2008/12/19", "$90,560"],
  ["9497", "2013/03/03", "$342,000"],
  ["6741", "2008/10/16", "$470,600"],
  ["3597", "2012/12/18", "$313,500"],
  ["1965", "2010/03/17", "$385,750"],
  ["1581", "2012/11/27", "$198,500"],
  ["3059", "2010/06/09", "$725,000"],
  ["1721", "2009/04/10", "$237,500"],
  ["2558", "2012/10/13", "$132,000"],
  ["2290", "2012/09/26", "$217,500"],
  ["1937", "2011/09/03", "$345,000"],
  ["6154", "2009/06/25", "$675,000"],
  ["8330", "2011/12/12", "$106,450"],
  ["3023", "2010/09/20", "$85,600"],
  ["5797", "2009/10/09", "$1,200,000"],
  ["8822", "2010/12/22", "$92,575"],
  ["9239", "2010/11/14", "$357,650"],
  ["1314", "2011/06/07", "$206,850"],
  ["2947", "2010/03/11", "$850,000"],
  ["8899", "2011/08/14", "$163,000"],
  ["2769", "2011/06/02", "$95,400"],
  ["6832", "2009/10/22", "$114,500"],
  ["3606", "2011/05/07", "$145,000"],
  ["2860", "2008/10/26", "$235,500"],
  ["8240", "2011/03/09", "$324,050"],
  ["5384", "2009/12/09", "$85,675"],
];

function drawTable(data) {
  let thead = $("#table thead");
  thead.empty();
  let header = $("<tr>");
  for (let i = 0; i < headers.length; i++) {
    let th = $("<th>" + headers[i] + "</th>");
    header.append(th);
  }
  thead.append(header);

  let tbody = $("#table tbody");
  tbody.empty();

  data.forEach((row) => {
    let tr = $("<tr>");
    row.forEach((field) => {
      let td = $("<td>" + field + "</td>");
      tr.append(td);
    });
    tbody.append(tr);
  });

  let tfoot = $("#table tfoot");
  tfoot.empty();

  let tr = $("<tr>");
  for (let i = 0; i < dataSet[0].length; i++) {
    let td = $("<td>");
    let input = $("<input>");
    input.attr("placeholder", "Type to filter by col " + i);
    td.append(input);
    tr.append(td);
    input.change(function (event) {
      let d = [];
      dataSet.forEach((dset) => {
        if (dset[i].includes(event.currentTarget.value)) {
          d.push(dset);
        }
      });
      drawTable(d);
      drawHistogram(d, 2);
      updateCsv(d);
      drawScatter(d, 1, 2);
    });
  }
  tfoot.append(tr);
}

function drawHistogram(data, i) {
  $("#histogram").empty();
  let x = [];
  data.forEach((row) => {
    x.push(row[i]);
  });

  let trace = {
    x: x,
    type: "histogram",
    nbins: 20,
  };
  let traces = [trace];
  Plotly.newPlot("histogram", traces);
}

function updateCsv(data) {
  let csv = "";
  data.forEach(function (row) {
    csv += row.join(",");
    csv += "\n";
  });

  let a = document.getElementById("export");
  a.href = "data:text/csv;charset=utf-8," + encodeURI(csv);
  a.download = "data.csv";
}

function drawScatter(data, i, j) {
  $("#scatter").empty();
  let x = [];
  let y = [];
  data.forEach((row) => {
    x.push(row[i]);
    y.push(row[j]);
  });

  var trace1 = {
    x: x,
    y: y,
    mode: "markers",
    type: "scatter",
  };

  var traces = [trace1];

  Plotly.newPlot("scatter", traces);
}

drawTable(dataSet);
drawHistogram(dataSet, 2);
updateCsv(dataSet);
drawScatter(dataSet, 1, 2);
