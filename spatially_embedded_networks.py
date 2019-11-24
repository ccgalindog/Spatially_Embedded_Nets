import networkx as nx
import numpy as np
import matplotlib.style as mpst
mpst.use('classic')
from matplotlib import pyplot as plt


def spatial_distance( ni, nj, x ):
	xi = x[ ni, : ]
	xj = x[ nj, : ]
	d_ij = np.linalg.norm( xi - xj )
	return d_ij

def redundancy_cost( N, G, x, r ):
	F = np.zeros( (N,N) )
	for i in range(N):
		for j in range(N):
			if (i != j) and ( G.has_edge( i, j ) == False):
				dg_ij = nx.shortest_path_length( G, source = i, target = j, weight = None ) 
				ds_ij = spatial_distance( i, j, x )
				if (ds_ij > 0):
					F[ i, j ] = ( ( dg_ij + 1 )**r )/ds_ij
	return F


def graph_initialization( N, p, q, r, s, x ):
	G = nx.Graph( )
	all_edges = []
	for node_i in range( N ):
		for node_j in range( N ):
			if node_i != node_j:
				d_ij = spatial_distance( node_i, node_j, x )
				all_edges.append( (node_i, node_j, d_ij) )
	G.add_weighted_edges_from( all_edges )
	if (N > 1):
		T = nx.minimum_spanning_tree( G ) #I2
	else:
		G.add_node(1)
		T = G
	if (nx.is_connected( T ) == False):
		print('Beware, minimum spanning tree is not connected')
	else:
		print('Minimum spanning tree created')
	m = int(np.floor( N*(1 - s)*(p + q) ))
	for a in range( m ): #I3
		print( 'Adding new links: ', 100*a/m, ' %' )
		F = redundancy_cost( N, T, x, r )
		if (np.max(F) > 0):
			link_dis = np.unravel_index( np.argmax( F ), F.shape )
			d_ij = spatial_distance( link_dis[0], link_dis[1], x )
			T.add_edge( link_dis[0], link_dis[1], weight = d_ij )
	return T

def graph_growth( G, NF, p, q, r, s, x, x_2add ):
	i = 0
	N = len(G.nodes)
	N_2_add = NF - N
	while (i < N_2_add):
		if ( np.random.rand( ) > s ): #G0
			xi = x_2add[i, :] #G1
			ds_all = np.array([ np.linalg.norm( xi - x[k] ) for k in range(len(x))])
			j = np.argmin( ds_all ) #G2
			G.add_node( N )
			G.add_edge( N, j, weight = ds_all[j] )
			N = N + 1
			x = np.concatenate( [ x, x_2add[i, :].reshape(1,-1) ], axis = 0 )
			if ( np.random.rand() < p ): #G3
				F = redundancy_cost( N, G, x, r )
				F = F[-1,:]
				if (np.max(F) > 0):
					link_dis = np.argmax( F )
					d_ij = spatial_distance( N-1, link_dis, x )
					G.add_edge( N-1, link_dis, weight = d_ij )

			if (np.random.rand() < q): #G4
				F = redundancy_cost( N, G, x, r )
				il = np.random.randint( 0, N )
				F = F[il,:]
				if (np.max(F) > 0):
					link_dis = np.argmax( F )
					d_ij = spatial_distance( N-1, link_dis, x )
					G.add_edge( il, link_dis, weight = d_ij )			
		else: #G5
			if (len(G.edges) > 0):
				rand_edge_ix = np.random.choice( len(G.edges) )
				all_edges = list(G.edges)
				rand_edge = all_edges[rand_edge_ix]
				xa = x[ rand_edge[0], : ]
				xb = x[ rand_edge[1], : ]
				G.remove_edge( rand_edge[0], rand_edge[1] )
				xi = ( xa + xb )/2
				G.add_node( N )
				N = N + 1
				#print( x.shape, xi.reshape(1,-1).shape )
				x = np.concatenate( [ x, xi.reshape(1,-1) ], axis = 0 )
				d_ij = spatial_distance( N-1, rand_edge[0], x )
				G.add_edge( N-1, rand_edge[0], weight = d_ij )
				d_ij = spatial_distance( N-1, rand_edge[1], x )
				G.add_edge( N-1, rand_edge[1], weight = d_ij )
		print( 'Current network size: ', N )
		i = i + 1
	return G, x


def create_synthetic_powergrid( N0, N, p, q, r, s, x0, x_2add ):
	'''
	Construct random spatially embedded graphs using the algorithm proposed in:
	* Schultz, P.; Heitzig, J.; Kurths, J. -- "A random growth model for power grids and other spatially embedded infrastructure networks". DOI: 10.1140/epjst/e2014-02279-6
	
	# Arguments:
	N0: int - nodes to be arranged in a minimum spanning tree.
	N: int - nodes of the final network.
	p: float in range [0,1] - probability of attaching an additional link to each new node added on each growth step
	q: float in range [0,1] - probability of constructing further redundant links between existing nodes on each growth step
	r: float - exponent for the cost-vs-redundancy trade-off function
	s: float in range [0,1] - probability of splitting an existing line on each growth step
	x0: numpy array with shape ( N0, 2 ) - geographic node locations for nodes in the minimum spanning tree [[x_1, y_1],[x_2, y_2], ...[x_N0, y_N0]]
	x_2add: numpy array with shape ( N-N0, 2 ) - geographic node locations for nodes added in the growth phase [[x_1, y_1],[x_2, y_2], ...[x_(N-N0), y_(N-N0)]]
	
	# Returns:
	G: networkx.Graph - Generated network structure.
	xf: numpy.array - Geographic locations of all nodes.
	'''

	G = graph_initialization( N0, p, q, r, s, x0 )
	G, x = graph_growth( G, N, p, q, r, s, x0, x_2add )

	return G, x

