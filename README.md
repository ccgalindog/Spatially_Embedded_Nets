# Spatially Embedded Networks

Python implementation of the algorithm proposed on:

```json @Article{Schultz2014,
author="Schultz, Paul,
and Heitzig, Jobst,
and Kurths, J{\"u}rgen",
title="A random growth model for power grids and other spatially embedded infrastructure networks",
journal="The European Physical Journal Special Topics",
year="2014",
month="Oct",
day="01",
volume="223",
number="12",
pages="2593--2610",
issn="1951-6401",
doi="10.1140/epjst/e2014-02279-6",
url="https://doi.org/10.1140/epjst/e2014-02279-6"
}
```

This algorithm generates random spatially embedded graphs with characteristics that resemble real-world infrastructure networks as power-grids. This is achieved by optimizing the redundancy/cost function:

<center><a href="https://www.codecogs.com/eqnedit.php?latex=f_{(i,j)}&space;=&space;\frac{(d_G(i,j)&plus;1))^r}{d_{spatial}(i,j)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f_{(i,j)}&space;=&space;\frac{(d_G(i,j)&plus;1))^r}{d_{spatial}(i,j)}" title="f_{(i,j)} = \frac{(d_G(i,j)+1))^r}{d_{spatial}(x_i,x_j)}" /></a></center>

Which represents a trade-off between the spatial distance and connection distance separating each pair of nodes *i* and *j*.

#### Input parameters:

N0: Number of nodes to be aranged initially in a Minimum Spanning Tree (MST).

N: int - Number of nodes of the final network.

p: float in range [0,1] - Probability of attaching an additional link to each new node added on each growth phase step.

q: float in range [0,1] - Probability of constructing further links between existing nodes on each growth phase step.

r: float - Exponent for the cost-vs-redundancy trade-off function.

s: float in range [0,1] - Probability of splitting an existing line on each growth step.

x0: numpy array with shape ( N0, 2 ) - geographic node locations for nodes in the minimum spanning tree [[x_1, y_1],[x_2, y_2], ...[x_N0, y_N0]].

x_2add: numpy array with shape ( N-N0, 2 ) - geographic node locations for nodes added in the growth phase [[x_1, y_1],[x_2, y_2], ...[x_(N-N0), y_(N-N0)]].


#### Returns:

G: networkx.Graph - Generated network structure.

xf: numpy.array - Geographic locations of all nodes.


<img src="https://github.com/ccgalindog/Spatially_Embedded_Nets/blob/master/Images/K_powergrid_N0_1_Nadd_199_p_0.6_q_0.4_r_1_s_0_.png" width="400" height="255" /><img src="https://github.com/ccgalindog/Spatially_Embedded_Nets/blob/master/Images/K_powergrid_N0_200_Nadd_0_p_0.6_q_0.4_r_0_s_0_.png" width="400" height="255" />





## How to use:

Just import the module `spatially_embedded_networks.py` and run the function `create_synthetic_powergrid( ... )` as shown in the example script `Test_Growth_Model.py`. 
