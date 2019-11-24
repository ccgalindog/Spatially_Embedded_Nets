import networkx as nx
import numpy as np
import matplotlib.style as mpst
mpst.use('classic')
from matplotlib import pyplot as plt
from spatially_embedded_networks import *

def main():
	N0 = 100 # Nodes to be located on a minimum spanning tree (MST)
	x0 = np.random.rand( N0, 2 ) # Geographic locations for the MST nodes
	N_add = 100 # Nodes to add in the growth phase
	x_2add = np.random.rand( N_add, 2 ) # Geographic locations for the nodes added on growth phase 
	N = N0 + N_add # Total number of nodes in the final graph
	# Building parameters:
	p = 0.6 
	q = 0.4 
	r = 1 
	s = 0.2 
	# build the spatially embedded graph:
	G, xf = create_synthetic_powergrid( N0, N, p, q, r, s, x0, x_2add )
	

	# Get the adjacency matrix and save it on a .txt file:
	K_matrix = nx.to_numpy_matrix(G)
	out_K_file = 'K_powergrid_N0_{}_Nadd_{}_p_{}_q_{}_r_{}_s_{}_.txt'.format( 
					N0, N_add, p, q, r, s )
	np.savetxt( out_K_file, K_matrix )

	# Get node degree distribution:
	degree_list = np.array(G.degree)
	degree_list = degree_list[:,1]


	# Plot the generated graph:
	fig = plt.figure()
	ax1 = fig.add_subplot(121)
	nx.draw( G, xf, node_size = 10, node_color = 'lime')

	ax1.annotate('$N_0 = {}, N = {}$'.format(
			N0, N),
			xy=(0.7, 0.0),  xycoords='data',
            xytext=(0.7, 0.0), textcoords='axes fraction',
            horizontalalignment='right', verticalalignment='top',
            )
	ax1.annotate('$p = {}, q = {}, r = {}, s = {}$'.format(
			p, q, r, s),
			xy=(0.7, -0.05),  xycoords='data',
            xytext=(0.7, -0.05), textcoords='axes fraction',
            horizontalalignment='right', verticalalignment='top',
            )


	ax2 = fig.add_subplot(122)
	plt.hist( degree_list, bins = np.max(degree_list)+1, color = 'navy' )
	ax2.yaxis.tick_right()
	ax2.yaxis.set_label_position("right")
	ax2.grid()
	ax2.set_xlabel(r'$k$', fontsize = 20)
	ax2.set_ylabel(r'$P_{(k)}$', fontsize = 20)
	plt.savefig( out_K_file.replace('.txt', '.png') )
	plt.tight_layout()
	plt.show()

if __name__ == '__main__':
	main()