# K_means
The K_means function creates clusters out of a given data points
This code includes a function of the K_means algoithm and an example for running it

Inputs:
data -list:                   a list of points in any desired dimention
K - integer:                  the number of clusters desired,
initial_c - list with arrays: defines the initial centers, 
max_iter - integer:           the maximum iterations alowd for the function to run

outputs:
c - list:              the final centers of the clusters
clusters - list:       the final clusters, each cluster includes the points that belongs to it
labels - array:        an array of the labels for every point, in the order as the points appear in data
iter_count - integer : the amount of iterations it took the algorithm to get to the final solution 
