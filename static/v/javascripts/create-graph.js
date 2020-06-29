/*
 * Parse the data and create a graph with the data.
 */
function parseData(createGraph) {
	Papa.parse("/static/v/javascripts/abcde.csv", {
		download: true,
		complete: function(results) {
			createGraph(results.data);
		}
	});
}

function createGraph(data) {
	var dates = ['date'];
	var price = ['price'];
	for (var i = 1; i < data.length; i++) {
	  if (data[i][0]==""){		
	  }  
	  else{
		dates.push(data[i][0])
		price.push(data[i][1]);
	  }		
		
	}

	console.log(dates);
	console.log(price);
	console.log(data.length);
	

	var chart = c3.generate({
		data: {
			x: 'date',
			xFormat: '%Y-%m-%d',
			columns: [
			dates,
           
            price
            
			]
		},
		axis: {
			x: {
				type: 'timeseries',
				// if true, treat x value as localtime (Default)
				// if false, convert to UTC internally
				localtime: false,
				tick: {
					format: '%Y-%m-%d'
				}
			}
		}
	});
}	

parseData(createGraph);