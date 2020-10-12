def K_means(data,K,initial_c,max_iter):
    import numpy as np
    #initialization
    iter_count=0
    improved=True
    improved_vec = np.zeros(K)
    for k in range(K):
        improved_vec[k]=True
    c=initial_c[:]
    
    # K means algorithm
    while improved:
        prev_c=c[:]
        iter_count = iter_count + 1
        print('iteration #'+str(iter_count))
       
        # update clusters according to centers
        clusters = []
        for k in range(K):
              clusters.append([])
        for i,sample in enumerate(data):       
            distances = np.zeros((K,1))
            for k in range(K):
                #calculate euclidian distances:
                dist=np.linalg.norm(np.asarray(sample)-c[k])
                distances[k]=dist
            wich_c = np.argmin(distances)
            clusters[wich_c].append(i)
        for k in range(K):
            if len(clusters[k])==0:
                raise ValueError('One of the clusters is empty, try again with differen K or different initial centers')

        #update centers according to new clusters:
        for k in range(K):
            indices=np.asarray(clusters[k])
            c[k]=np.mean([data[i] for i in indices],axis=0) 
        #check if the centers had changed, if not then stop the while loop
        for k in range(K):
            if np.any(prev_c[k] != c[k]):
                improved_vec[k] = True                         
            else:
                improved_vec[k] = False
        if np.any(improved_vec == True):
            improved = True
        else:
            improved = False
        if iter_count >= max_iter:
            improved = False
    
    labels=np.zeros(len(data))
    for k in range(K):
        dots_in_k = clusters[k]
        labels[dots_in_k]=k    
    
    return c,clusters,iter_count,labels

    
#example:
import numpy as np
K=3
data = [[1,10],[1,11],[2,9],[2,10],[6,19],[5,21],[5,20],[5,19],[50,-10],[55,-8],[52,-9]]
max_iter = 50
initial_c=[]
for i in range(K):
    initial_c.append(np.random.randint(np.argmax(data),size=np.size(data,1)))
centers,clusters,iter_count,labels=K_means(data,K,initial_c,max_iter)

#plot the example
import pylab as pl
for i in range(len(data)):
    if(labels[i] == 0):
        c1 = pl.scatter(data[i][0],data[i][1],c='r',marker='o')
    elif(labels[i] == 1):
        c2 = pl.scatter(data[i][0],data[i][1],c='g',marker='o')
    elif(labels[i] == 2):
        c3 = pl.scatter(data[i][0],data[i][1],c='b',marker='o')
pl.scatter(centers[0][0],centers[0][1],c='k',marker='x')
pl.scatter(centers[1][0],centers[1][1],c='k',marker='x')
pl.scatter(centers[2][0],centers[2][1],c='k',marker='x')

pl.legend([c1, c2,c3],['Cluster 1', 'Cluster 2','Cluster 3'])
pl.title('K-means clusters dataset into 3 clusters')
pl.show()




