



var svg = d3.select("#chart-area").append("svg")
    .attr("width", 400)
    .attr("height", 400)

var circle = svg.append("circle")
    .attr("cx", 200)
    .attr("cy", 200)
    .attr("r", 100)
    .attr("fill", "blue")

var rect = svg.append("rect")
    .attr("x", 10)
    .attr("y", 10)
    .attr("width", 50)
    .attr("height", 50)
    .attr("stroke-width", 5)
    .attr('fill', green)



