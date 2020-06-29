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
	var years = [];
	var silverMinted = [];

	for (var i = 1; i < data.length; i++) {
		years.push(data[i][0]);
		silverMinted.push(data[i][1]);
	}

	console.log(years);
	console.log(silverMinted);
	price=['anything', 30, 200, 100, 400, 150, 250];
	dates=['u', '2012-12-31', '2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04', '2013-01-05'];

	var chart = c3.generate({
		data: {
			x: 'u',
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
					format: '%d-%m-%Y'
				}
			}
		}
	});
}	

parseData(createGraph);