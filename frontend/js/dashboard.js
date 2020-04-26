var baseURL = "http://localhost:5000/twitter-sentiment-analysis/v1/";

$(document).ready(function(){

	if (sessionStorage.getItem("firstName") == null) {
		swal("Warning!", "Your session has expired, please sign in again.", "warning");
	  	window.setTimeout(function(){
         	window.location.replace("index.html");
        }, 2000);
	}
	else{

		$('#user-message').text('Hi, '+ sessionStorage.getItem("firstName") +'!');
		if(sessionStorage.getItem("is_admin") == 0 || sessionStorage.getItem("is_admin") == null)
		{
			$('#admin-panel').hide();
		}
	  	pieChart();
	  	columnChart();
	  	wordcloudChart();
	  	getTimeseriesChart();
	  	populateHasgtagTableData();
	}

});

function pieChart()
{
	var settings = {
	  "async": true,
	  "crossDomain": true,
	  "url": baseURL + "get-pie-chart-data",
	  "method": "GET",
	  "headers": {
	    "cache-control": "no-cache"
	  }
	};

	$.ajax(settings).done(function (response) {
	  if (response.status)
	  {
	  	Highcharts.chart('pie-chart', {
		    chart: {
		        plotBackgroundColor: null,
		        plotBorderWidth: null,
		        plotShadow: false,
		        type: 'pie',
		        backgroundColor: {
		            linearGradient: { x1: 0, y1: 0, x2: 1, y2: 1 },
		            stops: [
		                [0, '#363638'],
		                [1, '#363638']
		            ]
		        },
		        style: {
		            fontFamily: '\'Unica One\', sans-serif'
		        },
		        plotBorderColor: '#363638'
		    },
		    title: {
		        text: 'Sentiment Analysis Percentage-wise',
		        style: {
		            color: '#E0E0E3',
		            textTransform: 'uppercase',
		            fontSize: '20px'
        		}
		    },
		    credits: {
			     enabled: false
			},
		    tooltip: {
		        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>',
		        backgroundColor: 'rgba(0, 0, 0, 0.85)',
		        style: {
		            color: '#F0F0F0'
		        }
		    },
		    accessibility: {
		        point: {
		            valueSuffix: '%'
		        }
		    },
		    plotOptions: {
		        pie: {
		            allowPointSelect: true,
		            cursor: 'pointer',
		            dataLabels: {
		                enabled: true,
		                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
		            }
		        },
		        series: {
		            dataLabels: {
		                color: '#F0F0F3',
		                style: {
		                    fontSize: '13px'
		                }
		            },
		            marker: {
		                lineColor: '#333'
		            }
		        },
		        boxplot: {
		            fillColor: '#505053'
		        },
		        candlestick: {
		            lineColor: 'white'
		        },
		        errorbar: {
		            color: 'white'
		        }
		    },
		    series: [{
		        name: 'Sentiments',
		        colorByPoint: true,
		        data: response.data
		    }]
		});
	  }
	});
}

function columnChart()
{
	var settings = {
	  "async": true,
	  "crossDomain": true,
	  "url": baseURL + "get-column-chart-data",
	  "method": "GET",
	  "headers": {
	    "cache-control": "no-cache"
	  }
	}

	$.ajax(settings).done(function (response) {
	  if (response.status) {

	  	var data = response.data;
	  	var total_tweets = 0;
	  	$.each(response.data,function(key,value){
	  		total_tweets = total_tweets + value.y;
	  		if(value.name == "Neutral"){
	  			$('#neutral-tweets').text(value.y);
	  		}
	  		else if (value.name == "Positive") {
	  			$('#positive-tweets').text(value.y);
	  		}
	  		else{
	  			$('#negative-tweets').text(value.y);
	  		}
	  	});
	  	$('#total-tweets').text(total_tweets);

	  	Highcharts.chart('column-chart', {
		    chart: {
		        type: 'column',
		        backgroundColor: {
		            linearGradient: { x1: 0, y1: 0, x2: 1, y2: 1 },
		            stops: [
		                [0, '#363638'],
		                [1, '#363638']
		            ]
		        },
		        style: {
		            fontFamily: '\'Unica One\', sans-serif'
		        },
		        plotBorderColor: '#363638'
		    },
		    title: {
		        text: 'Sentiment Count',
		        style: {
		            color: '#E0E0E3',
		            textTransform: 'uppercase',
		            fontSize: '20px'
		        }
		    },
		    credits:{
		    	enabled: false
		    },
		    accessibility: {
		        announceNewData: {
		            enabled: true
		        }
		    },
		    xAxis: {
		        type: 'category',
		        // gridLineColor: '#707073',
		        labels: {
		            style: {
		                color: '#E0E0E3'
		            }
		        },
		        title: {
		            style: {
		                color: '#A0A0A3'
		            }
		        }
		    },
		    yAxis: {
		        labels: {
		            style: {
		                color: '#E0E0E3'
		            }
		        },
		        title: {
		        	text: 'Total no. of tweets',
		            style: {
		                color: '#A0A0A3'
		            }
		        }

		    },
		    legend: {
		        enabled: false
		    },
		    plotOptions: {
		        series: {
		            dataLabels: {
		            	enabled: true,
		                format: '{point.y}',
		                color: '#F0F0F3',
		                style: {
		                    fontSize: '13px'
		                }
		            },
		            marker: {
		                lineColor: '#333'
		            }
		        },
		        boxplot: {
		            fillColor: '#505053'
		        },
		        candlestick: {
		            lineColor: 'white'
		        },
		        errorbar: {
		            color: 'white'
		        }
		    },

		    tooltip: {
		        headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
		        pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y}<br/>',
	         	backgroundColor: 'rgba(0, 0, 0, 0.85)',
		        style: {
		            color: '#F0F0F0'
		        }
		    },

		    series: [
		        {
		            name: "Sentiments",
		            colorByPoint: true,
		            data: response.data
		       }]
		});
	  }
	});
}

function populateHasgtagTableData()
{
	var settings = {
	  "async": true,
	  "crossDomain": true,
	  "url": baseURL + "get-twitter-users-data",
	  "method": "GET",
	  "headers": {
	    "cache-control": "no-cache"
	  }
	}

	$.ajax(settings).done(function (response) {
	  var hashtag_data = "";
	   $.each(response.data,function(key,value){
	   	hashtag_data += "<tbody>";
	   	if (value.sentiment == "Positive") {
	   		hashtag_data += "<tr style=\"background-color : #363638; color: #39ff14;\">";
	   	}
	   	else if (value.sentiment == "Negative") {
	   		hashtag_data += "<tr style=\"background-color : #363638; color: #ff073a;\">";
	   	}
	   	else{
	   		hashtag_data += "<tr style=\"background-color : #363638; color: #9CC0E7;\">";
	   	}
		hashtag_data += "<td><img src="+value.profile_image+"></td>";
		hashtag_data += "<td>"+value.screen_name+"</td>";
		hashtag_data += "<td>"+value.user_description+"</td>";
		hashtag_data += "<td>"+value.location+"</td>";
		hashtag_data += "<td>"+value.no_of_friends+"</td>";
		// hashtag_data += "<td>"+value.no_of_followers+"</td>"
		// hashtag_data += "<td>"+value.no_of_favourites+"</td>"
		hashtag_data += "<td>"+value.tweet_creation_time+"</td>";
		hashtag_data += "<td>"+value.tweet_text+"</td>";
		// hashtag_data += "<td>"+value.no_of_retweet+"</td>";
		hashtag_data += "<td>"+value.sentiment+"</td>";
	  	hashtag_data += "</tbody>";
	  	hashtag_data += "</tr>";
	   });
	   $('#hashtagtable').append(hashtag_data);
	   // $('#hashtagtable').DataTable({
	   // });
	   var table = $('#hashtagtable').dataTable({
	   	"paging":   false,
	   	"searching": false,
	   	"showNEntries" : false,
	   	"info": false,
	   	"sorting":false,
	   	"filtering":false,
	   	"ordering":false,
	   	"scrollY": "500px"
	   });
	    var tableTools = new $.fn.dataTable.TableTools(table, {
	        'aButtons': [
	            {
	                'sExtends': 'xls',
	                'sButtonText': 'Save to Excel',
	                'sFileName': 'Data.xls',
	            },
	            {
	                'sExtends': 'print',
	                'bShowAll': true,
	            },
	            {
	                'sExtends': 'pdf',
	                'bFooter': false,
	                'bShowAll': true,
	            },
	            'csv'
	        ],
	        'sSwfPath': 'https://cdn.datatables.net/tabletools/2.2.4/swf/copy_csv_xls_pdf.swf'
	    });
        $(tableTools.fnContainer()).insertBefore('#hashtagtable');
	});
}

function wordcloudChart()
{
	var settings = {
	  "async": true,
	  "crossDomain": true,
	  "url": baseURL + "get-wordcloud-data",
	  "method": "GET",
	  "headers": {
	    "cache-control": "no-cache"
	  }
	}

	$.ajax(settings).done(function (response) {
	  if (response.status) {
	  	var text = response.data;
	  	var lines = text.split(/[,\. ]+/g),
	    data = Highcharts.reduce(lines, function (arr, word) {
	        var obj = Highcharts.find(arr, function (obj) {
	            return obj.name === word;
	        });
	        if (obj) {
	            obj.weight += 1;
	        } else {
	            obj = {
	                name: word,
	                weight: 1
	            };
	            arr.push(obj);
	        }
	        return arr;
	    }, []);

	    Highcharts.chart('wordcloud-chart', {
		    accessibility: {
		        screenReaderSection: {
		            beforeChartFormat: '<h5>{chartTitle}</h5>' +
		                '<div>{chartSubtitle}</div>' +
		                '<div>{chartLongdesc}</div>' +
		                '<div>{viewTableButton}</div>'
		        }
		    },
		    series: [{
		        type: 'wordcloud',
		        data: data,
		        name: 'Occurrences'
		    }],
		    title: {
		        text: 'Wordcloud of All Tweets',
		        style: {
		            color: '#E0E0E3',
		            textTransform: 'uppercase',
		            fontSize: '20px'
		        }
		    },
		    colors: ['#2b908f', '#90ee7e', '#f45b5b', '#7798BF', '#aaeeee', '#ff0066',
		        '#eeaaee', '#55BF3B', '#DF5353', '#7798BF', '#aaeeee'],
		    chart: {
		        backgroundColor: {
		            linearGradient: { x1: 0, y1: 0, x2: 1, y2: 1 },
		            stops: [
		                [0, '#363638'],
		                [1, '#363638']
		            ]
		        },
		        style: {
		            fontFamily: '\'Unica One\', sans-serif'
		        },
		        plotBorderColor: '#606063'
		    },
		    xAxis: {
		        gridLineColor: '#707073',
		        labels: {
		            style: {
		                color: '#E0E0E3'
		            }
		        },
		        lineColor: '#707073',
		        minorGridLineColor: '#505053',
		        tickColor: '#707073',
		        title: {
		            style: {
		                color: '#A0A0A3'
		            }
		        }
		    },
		    yAxis: {
		        gridLineColor: '#707073',
		        labels: {
		            style: {
		                color: '#E0E0E3'
		            }
		        },
		        lineColor: '#707073',
		        minorGridLineColor: '#505053',
		        tickColor: '#707073',
		        tickWidth: 1,
		        title: {
		            style: {
		                color: '#A0A0A3'
		            }
		        }
		    },
		    tooltip: {
		        backgroundColor: 'rgba(0, 0, 0, 0.85)',
		        style: {
		            color: '#F0F0F0'
		        }
		    },
		    plotOptions: {
		        series: {
		            dataLabels: {
		                color: '#F0F0F3',
		                style: {
		                    fontSize: '13px'
		                }
		            },
		            marker: {
		                lineColor: '#333'
		            }
		        },
		        boxplot: {
		            fillColor: '#505053'
		        },
		        candlestick: {
		            lineColor: 'white'
		        },
		        errorbar: {
		            color: 'white'
		        }
		    },
		    legend: {
		        backgroundColor: 'rgba(0, 0, 0, 0.5)',
		        itemStyle: {
		            color: '#E0E0E3'
		        },
		        itemHoverStyle: {
		            color: '#FFF'
		        },
		        itemHiddenStyle: {
		            color: '#606063'
		        },
		        title: {
		            style: {
		                color: '#C0C0C0'
		            }
		        }
		    },
		    credits: {
		        enabled: false
		    },
		    labels: {
		        style: {
		            color: '#707073'
		        }
		    },
		    drilldown: {
		        activeAxisLabelStyle: {
		            color: '#F0F0F3'
		        },
		        activeDataLabelStyle: {
		            color: '#F0F0F3'
		        }
		    },
		    navigation: {
		        buttonOptions: {
		            symbolStroke: '#DDDDDD',
		            theme: {
		                fill: '#505053'
		            }
		        }
		    },
		    // scroll charts
		    rangeSelector: {
		        buttonTheme: {
		            fill: '#505053',
		            stroke: '#000000',
		            style: {
		                color: '#CCC'
		            },
		            states: {
		                hover: {
		                    fill: '#707073',
		                    stroke: '#000000',
		                    style: {
		                        color: 'white'
		                    }
		                },
		                select: {
		                    fill: '#000003',
		                    stroke: '#000000',
		                    style: {
		                        color: 'white'
		                    }
		                }
		            }
		        },
		        inputBoxBorderColor: '#505053',
		        inputStyle: {
		            backgroundColor: '#333',
		            color: 'silver'
		        },
		        labelStyle: {
		            color: 'silver'
		        }
		    },
		    navigator: {
		        handles: {
		            backgroundColor: '#666',
		            borderColor: '#AAA'
		        },
		        outlineColor: '#CCC',
		        maskFill: 'rgba(255,255,255,0.1)',
		        series: {
		            color: '#7798BF',
		            lineColor: '#A6C7ED'
		        },
		        xAxis: {
		            gridLineColor: '#505053'
		        }
		    },
		    scrollbar: {
		        barBackgroundColor: '#808083',
		        barBorderColor: '#808083',
		        buttonArrowColor: '#CCC',
		        buttonBackgroundColor: '#606063',
		        buttonBorderColor: '#606063',
		        rifleColor: '#FFF',
		        trackBackgroundColor: '#404043',
		        trackBorderColor: '#404043'
		    }
		});

	  }
	});
}

function getTimeseriesChart()
{
	var settings = {
	  "async": true,
	  "crossDomain": true,
	  "url": baseURL + "get-timeseries-data",
	  "method": "GET",
	  "headers": {
	    "cache-control": "no-cache"
	  }
	}

	$.ajax(settings).done(function (response) {
	  if (response.status) {
	  	Highcharts.chart('timeseries-chart', {
            chart: {
                zoomType: 'x',
                backgroundColor: {
		            linearGradient: { x1: 0, y1: 0, x2: 1, y2: 1 },
		            stops: [
		                [0, '#363638'],
		                [1, '#363638']
		            ]
		        },
		        style: {
		            fontFamily: '\'Unica One\', sans-serif'
		        },
		        plotBorderColor: '#606063'
            },
            title: {
                text: 'Count of Tweets by Date',
                style: {
		            color: '#E0E0E3',
		            textTransform: 'uppercase',
		            fontSize: '20px'
		        }
            },
            xAxis: {
                type: 'datetime',
                gridLineColor: '#707073',
		        labels: {
		            style: {
		                color: '#E0E0E3'
		            }
		        },
		        lineColor: '#707073',
		        minorGridLineColor: '#505053',
		        tickColor: '#707073',
		        title: {
		            style: {
		                color: '#A0A0A3'
		            }
		        }
            },
            yAxis: {
                title: {
                    text: 'Count of Tweets'
                },
                gridLineColor: '#707073',
		        labels: {
		            style: {
		                color: '#E0E0E3'
		            }
		        },
		        lineColor: '#707073',
		        minorGridLineColor: '#505053',
		        tickColor: '#707073',
		        tickWidth: 1,
		        title: {
		            style: {
		                color: '#A0A0A3'
		            }
		        }
            },
            tooltip: {
		        backgroundColor: 'rgba(0, 0, 0, 0.85)',
		        style: {
		            color: '#F0F0F0'
		        }
		    },
		    credits: {
		        enabled:false
		    },
            legend: {
                enabled: false,
                backgroundColor: 'rgba(0, 0, 0, 0.5)',
		        itemStyle: {
		            color: '#E0E0E3'
		        },
		        itemHoverStyle: {
		            color: '#FFF'
		        },
		        itemHiddenStyle: {
		            color: '#606063'
		        },
		        title: {
		            style: {
		                color: '#C0C0C0'
		            }
		        }
            },
            plotOptions: {
                area: {
                    fillColor: {
                        linearGradient: {
                            x1: 0,
                            y1: 0,
                            x2: 0,
                            y2: 1
                        },
                        stops: [
                            [0, Highcharts.getOptions().colors[0]],
                            [1, Highcharts.color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
                        ]
                    },
                    marker: {
                        radius: 2
                    },
                    lineWidth: 1,
                    states: {
                        hover: {
                            lineWidth: 1
                        }
                    },
                    threshold: null
                },
                series: {
		            dataLabels: {
		                color: '#F0F0F3',
		                style: {
		                    fontSize: '13px'
		                }
		            },
		            marker: {
		                lineColor: '#333'
		            }
		        },
		        boxplot: {
		            fillColor: '#505053'
		        },
		        candlestick: {
		            lineColor: 'white'
		        },
		        errorbar: {
		            color: 'white'
		        }
            },
            labels: {
		        style: {
		            color: '#707073'
		        }
		    },
		    drilldown: {
		        activeAxisLabelStyle: {
		            color: '#F0F0F3'
		        },
		        activeDataLabelStyle: {
		            color: '#F0F0F3'
		        }
		    },
		    navigation: {
		        buttonOptions: {
		            symbolStroke: '#DDDDDD',
		            theme: {
		                fill: '#505053'
		            }
		        }
		    },
		    // scroll charts
		    rangeSelector: {
		        buttonTheme: {
		            fill: '#505053',
		            stroke: '#000000',
		            style: {
		                color: '#CCC'
		            },
		            states: {
		                hover: {
		                    fill: '#707073',
		                    stroke: '#000000',
		                    style: {
		                        color: 'white'
		                    }
		                },
		                select: {
		                    fill: '#000003',
		                    stroke: '#000000',
		                    style: {
		                        color: 'white'
		                    }
		                }
		            }
		        },
		        inputBoxBorderColor: '#505053',
		        inputStyle: {
		            backgroundColor: '#333',
		            color: 'silver'
		        },
		        labelStyle: {
		            color: 'silver'
		        }
		    },
		    navigator: {
		        handles: {
		            backgroundColor: '#666',
		            borderColor: '#AAA'
		        },
		        outlineColor: '#CCC',
		        maskFill: 'rgba(255,255,255,0.1)',
		        series: {
		            color: '#7798BF',
		            lineColor: '#A6C7ED'
		        },
		        xAxis: {
		            gridLineColor: '#505053'
		        }
		    },
		    scrollbar: {
		        barBackgroundColor: '#808083',
		        barBorderColor: '#808083',
		        buttonArrowColor: '#CCC',
		        buttonBackgroundColor: '#606063',
		        buttonBorderColor: '#606063',
		        rifleColor: '#FFF',
		        trackBackgroundColor: '#404043',
		        trackBorderColor: '#404043'
		    },
            series: [{
                type: 'area',
                name: 'Total Tweet Posted',
                data: response.data
            }]
        });
	  }
	});
}

function logout()
{
	swal("Success!", "You are successfully logged out.", "success");
	sessionStorage.getItem("firstName") = null;
	sessionStorage.getItem("is_admin") = null;
  	window.setTimeout(function(){
     	window.location.replace("index.html");
    }, 2000);
}