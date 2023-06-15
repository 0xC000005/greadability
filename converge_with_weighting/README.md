Graph readability metrics can be used to check the convergence rate of graph layout algorithms. This example uses [Greadability.js](https://github.com/rpgove/greadability) to calculate four graph layout readability metrics at each iteration of the [D3's force-directed graph layout algorithm](https://github.com/d3/d3-force/):

* *Edge crossings* measures the fraction of edges that cross (intersect) out of an approximate maximum number that can cross.
* *Edge crossing angle* measures the mean deviation of edge crossing angles from the ideal edge crossing angle (70 degrees).
* *Angular resolution (minimum)* measures the mean deviation of adjacent incident edge angles from the ideal minimum angles (360 degrees divided by the degree of that node).
* *Angular resoluction (deviation)* measures the average deviation of angles between incident
edges on each vertex.