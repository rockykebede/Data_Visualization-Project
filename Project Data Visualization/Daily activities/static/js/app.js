// Getting references from index html file for the metadata

var PanelData = d3.select("#sample-metadata");

// Using function to fetch the metada route to select Status
// from app.py

function buildMetadata(sample) {
  d3.json(`/metadata/${sample}`).then((values) => {
      
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

function buildCharts(combined) {
  d3.json(`/samples/${sample}`).then((values) => {
    const acitivity_IDS = values.acitivity_IDS;
    const activity_labels = values.activity_labels;
    const sample_values = values.sample_values;
    console.log(activity_labels,acitivity_IDS,sample_values);

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
// This code is given in the starter code 
function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");

  // Use the list of sample names to populate the select options
  d3.json("/names").then((sampleNames) => {
    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
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
