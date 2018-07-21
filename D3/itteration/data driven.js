

d3.csv("data/ages.csv").then(function(data))

var svg = d3.select("#chart-area").append("svg")
    .attr("width", 400)
    .attr("height", 400)

var circles = svg.selectAll("circle")
    .data(data)

circles.enter()
    .append("circle")
        .attr("cx", function(d, i){
            return (i * 50) + 25
        })
        .attr("cy", 25)
        .attr("r", function(d, i){
            return d
        })
        .attr("fill", "blue")





