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

This algorithm generates random spatially embedded graphs with characteristics that resemble real-world infrastructure networks as power-grids.

Parameters:

```math $N_0$ ``` - Number of nodes to be aranged initially in a Minimum Spanning Tree (MST).

The procedure is composed of 2 phases: 

*1. Initialization:* Here $N$ nodes are placed on a MST and $m = N_0(1-s)(p+q)$ extra edges are added between nodes with maximum $f_{(i,j)}$. 

and growth.


## How to use:

Just import the module `spatially_embedded_networks.py` and run the function `create_synthetic_powergrid( ... )` as shown in the example script `Test_Growth_Model.py`. 
