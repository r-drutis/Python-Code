#Function takes in a dissimilarity map as an dictionary.
#Uses upgma to produce the phylogenetic tree corresponding to the
#dissimilarity map.

#Return value will be a string representing a graph, using nested
#parantheses to denote level.

#Calculate closest clusters: Input dissimilarity map from newick files
#m = cluster(?)
#n = node
def closest_cluster(dis_map, m, n):
	best_distance = float('inf')	#pre set as highest possible value
	best_cluster = (-1, -1)			# shortest distance

	# goes through all combinations in the dist map
	for key in dis_map:
		(i, j) = key
		if (i == j):	# skip if it's the same keys (ex A, A)
			continue 
		# looks for the minimum in the current dis_map
		dist = dis_map[(i,j)]
		if dist < best_distance:	# track smallest distance
			best_distance = dist
			best_cluster = (i,j)	# set the best cluster as the one with the least distance
	return best_cluster, best_distance

def upgma(dis_map, m, n):
#Table for going between matrix index and cluster index 	
	upgma_tree = {}
	clusters = () 
	for i in n:
#represents the leaves. (node,child1,child2,height,size). -1 indicates no child 
		upgma_tree[i] = (-1, -1, 0, 1) # start with 1 node, no children

	current_map = dis_map 	# dis_map starts as current map, current map gets smaller
	new_cluster = n
	while len(clusters) > 2:
		(i,j), distance = closest_cluster(current_map, m, n)	# finds the key:value with lowest distance
		i_size = upgma_tree[i][3]	# calculate size with closest cluster coordinates
		j_size = upgma_tree[j][3]
#add the new cluster to the output leave list, with appropriate height 
		upgma_tree[new_cluster] = (i, j, distance / 2.0, i_size + j_size)
		
#update the dis map by removing min_i,min_j and adding new letter to the matrix 	
		clusters.remove(i)
		clusters.remove(j)

		# make new distance map with clusters set (with last clusters removed)
		new_dis_map = {}
		for a in clusters:
			for b in clusters:
				new_dis_map[(a,b)] = current_map[(a,b)]

		for a in clusters:
			new_dis_map[(new_cluster, a)] = (current_map[(i, a)] * i_size + current_map[(j, a)] * j_size)  / float(i_size + j_size)
			new_dis_map[(a, new_cluster)] = new_dis_map[(new_cluster, a)]

		new_dis_map[(new_cluster, new_cluster)] = 0

		clusters.append(new_cluster)
		current_map = new_dis_map
 #shift the rest of the clusters over by 1 
		new_cluster += 1
	
	(i,j), distance = closest_cluster(current_map, m, n)
	#try:
	i_size = upgma_tree.get(i,[3])
	j_size = upgma_tree.get(j,[3])
	#except KeyError:
		#pass
 #Now there are two remaining indices. We combine them and add them to the out list. 
	upgma_tree[new_cluster] = (i, j, distance / 2.0, i_size + j_size)

	return upgma_tree




"""
MAIN
"""

#Newick Format test file
test_map = {
	(0,0): 0,
	(0,1): 6,
	(0,2): 4,
	(0,3): 2,
	(1,0): 6,
	(1,1): 0,
	(1,2): 1,
	(1,3): 3,
	(2,0): 4,
	(2,1): 1,
	(2,2): 0,
	(2,3): 5,
	(3,0): 2,
	(3,1): 3,
	(3,2): 5,
	(3,3): 0
}

print (upgma(test_map, 4, 4))