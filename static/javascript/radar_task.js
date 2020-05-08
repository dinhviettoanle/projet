function initiate_radar(id_selected, info_project){
   var data = [{
      type: 'scatterpolar'
   }];
   Plotly.newPlot("div_plot", data);
}



function plot_radar(id_selected, info_project){

   // Initialisation des donnees
   var selected_project = info_project[info_project.findIndex(proj => proj.id === id_selected)];

   var members = [];
   var num_tasks = [];

   selected_project.members.forEach((item, index) => {
      members.push(item.name);
      num_tasks.push(parseInt(item.count));
   })

   members.push(selected_project.members[0].name);
   num_tasks.push(selected_project.members[0].count);


   // Plot
   var data = [{
      type: 'scatterpolar',
      r: num_tasks,
      theta: members,
      name: selected_project.name,
      fill: 'toself',
      hovertemplate : "Utilisateur : %{theta}<br>Nombre de tâches : %{r}"
   }];

   var layout = {
      polar : {
      radialaxis: {
         visible: true,
         range: [0, 7]
         }
      },
      showlegend: false,
      title : selected_project.name
   };

   var config = {
      responsive: true,
      displayModeBar : false
   };

   Plotly.newPlot("div_plot", data, layout, config);
}



function plot_histogram(id_selected, info_project){
   var selected_project = info_project[info_project.findIndex(proj => proj.id === id_selected)];

   var members = [];
   var num_tasks = [];

   selected_project.members.forEach((item, index) => {
      members.push(item.name);
      num_tasks.push(parseInt(item.count));
   })

   var data = [{
      type: 'bar',
      x : members,
      y : num_tasks,
      text: num_tasks.map(String),
      textposition: 'auto',
      hoverinfo: 'none',
      marker: {
         color: 'rgb(127,127,127)',
         opacity: 0.6,
         line: {
            color: 'rgb(80,80,80)',
            width: 1.5
         }
      }
   }];

   var layout = {
      showlegend: false,
      title : selected_project.name,
      xaxis: {
         tickangle: -45
      },
      yaxis: {
         title: '# de tâches'
      },
      bargap :0.05
   };

   var config = {
      responsive: true,
      displayModeBar : false
   };

   Plotly.newPlot('div_plot', data, layout, config);
}
