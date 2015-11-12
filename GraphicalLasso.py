#Implement the vanilla Graphical Lasso algorithm; more tweaks to follow soon;
import csv
import sys
import numpy as np
import sklearn as sl

#calculate covariance:
rho = 0.01
stop_criterion = 0.001
max_iter = 500

datamatrix=datamatrix.T
S=np.cov(datamatrix)
W=S + rho*np.eye(len(S), dtype = int)
W_old = W

#prepare for loops

for iter in xrange(max_iter):
    #working on one col/row at a time
    #and cut W into four parts: W11, W12, (W21), W22
    for col in xrange(len(W)):
        W11_indices = np.setdiff1d(range(len(W)), col)
        W11 = W[W11_indices,W11_indices]
        s12 = W[col, W11_indices]
        #solve using coordinate descent: according to Friedman 2007
        beta = sl.linear_model.lasso_path(W11, s12, rho) 
        #get the last column
        beta = beta[:,-1]

        W[col, W11_indices] = np.dot(W11, beta)
        W[W11_indices, col] = np.transpose(W[col, W11_indices])
    #test stop criterion
    if np.linalg.norm(W_old-W)<stop_criterion:
        break;
    W_old = W

#final result:
Theta = np.inv(W)











        
        

