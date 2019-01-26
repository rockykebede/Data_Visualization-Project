// Getting references from index html file for the metadata

var PanelData = d3.select("#sample-metadata");

// Using function to fetch the metada route to select Status
// from app.py

function buildMetadata(Status) {
  d3.json(`/combined/${Status}`).then((values) => {
      
    // Use `.html("") to clear any existing data
    PanelData.html("");

    // Using `Object.entries` and 'for each' to add 
    //each key and value pair to the PanelData
    //append the fetch data to the h6 element
    
    Object.entries(values).forEach(([key, val]) => {
      PanelData.append("h6").text(`${key}: ${val}`);
      console.log(key,val);
    });

    
  });
}
// Using d3 json to build the bubble and pie charts
// from app.y sample route and use constant variables to build the charts

function buildCharts(Status) {
  d3.json(`/samples/${Status}`).then((values) => {
    const acitivity_IDS = values.acitivity_IDS;
    const activity_labels = values.activity_labels;
    const sample_values = values.sample_values;
    console.log(activity_labels,acitivity_IDS,sample_values);

  // Bubble Chart
  var bubbleChartLayout = {
      title: 'Daily Activities Bubble Chart',
      height: 700,
      width: 1200,
      showlegend: true,
      hoverinfo: "activity_labels",
               
    };
    var bubbleChartData = [
      {
        x: acitivity_IDS,
        y: sample_values,
        text: activity_labels,
        mode: "markers",
        marker: {
          size: sample_values,
          color: acitivity_IDS,
          colorscale: "Rainbow"
        }
      }
    ];


   //Using plotly.plot selecting the bubble elment and passing
   //the bubble chart data and the bubble chart layout for that selected sample
    Plotly.plot("bubble", bubbleChartData, bubbleChartLayout);


  var pieChartLayout = {
      title: "Daily Activities Pie Chart",
      height: 600,
      width: 800
    };
  var pieChartData = [
      {
        
        values: sample_values,
        labels: acitivity_IDS,
        hoverinfo: "activity_labels",
        type: "pie"
      }
    ]; 
   //Using plotly.plot selecting the pie elment and passing
   //the pie chart data and the pie chart layout for that selected Status
    Plotly.plot("pie", pieChartData, pieChartLayout);
  });
}

function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");

  // Use the list of sample names to populate the select options
  d3.json("/names").then((sampleNames) => {
    sampleNames.forEach((Status) => {
      selector
        .append("option")
        .text(Status)
        .property("value", Status);
    });

    // Use the first sample from the list to build the initial plots
    const firstSample = sampleNames[0];
    buildCharts(firstSample);
    buildMetadata(firstSample);
  });
}

function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  buildCharts(newSample);
  buildMetadata(newSample);
}

// Initialize the dashboard
init();
