 google.charts.load('current', {'packages':['table','corechart', 'bar']});
      google.charts.setOnLoadCallback(drawBasic);
	  google.charts.setOnLoadCallback(drawTable);

	  function drawBasic() {

      var datas = new google.visualization.DataTable();
        datas.addColumn('string', 'Word');
        datas.addColumn('number', 'Frequency');
        datas.addRows({{ adjs }})

      var options = {
        title: 'Words Most Useds to Describe Professor',
        width: 500,
		height: 400,
		chartArea: {width: '60%'},
        hAxis: {
          title: 'Frequency',
          minValue: 0
        },
		legend: { position: "none" },
        vAxis: {
          title: 'Words'
        }
      };

      var chart = new google.visualization.BarChart(document.getElementById('chart_div'));

      chart.draw(datas, options);
    }
    
	  
      function drawTable() {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Word');
        data.addColumn('number', 'Frequency');
        data.addRows([['tough', 3],
 ['few', 2],
 ['clear', 2],
 ['nice', 2],
 ['useful', 1],
 ['challenging', 1],
 ['simple', 1],
 ['awesome', 1],
 ['general', 1],
 ['high', 1],
 ['sure', 1]])
		data.setTableProperties({style: 'font-family: Montserrat, sans-serif;'})
        var table = new google.visualization.Table(document.getElementById('works_text'));

        table.draw(data, {showRowNumber: false, width: '100%', height: '40%'});
      }