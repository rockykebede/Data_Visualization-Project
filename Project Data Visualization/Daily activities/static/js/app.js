// Getting references 

var PanelData = d3.select("#sample-metadata");


function buildMetadata(Mstatus) {
  d3.json(`/combineddata/${Mstatus}`).then((values) => {
      
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

function buildCharts(Mstatus) {
  d3.json(`/activity_data/${Mstatus}`).then((values) => {
    const acitivity_IDS = values.acitivity_IDS;
    const activity_labels = values.activity_labels;
    const Mstatus_values = values.Mstatus_values;
    console.log(activity_labels,acitivity_IDS,Mstatus_values);

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
        y: Mstatus_values,
        text: activity_labels,
        mode: "markers",
        marker: {
          size: Mstatus_values,
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
        
        values: Mstatus_values,
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

  // Use the list of Marital Status to populate the select options
  d3.json("/maritalstatus").then((sampleNames) => {
    sampleNames.forEach((Status) => {
      selector
        .append("option")
        .text(Mstatus)
        .property("value", Mstatus);
    });

    // Use the first value from the list to build the initial plots
    const firstSample = sampleNames[0];
    buildCharts(firstSample);
    buildMetadata(firstSample);
  });
}

function optionChanged(newSample) {
  // Fetch new data each time a new marital Status is selected
  buildCharts(newSample);
  buildMetadata(newSample);
}

// Initialize the dashboard
init();
