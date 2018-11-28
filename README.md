Repository for the final project of the course-part1 

Supernova constraints to Omega matter

The goal is reproduce Figure 9, and table 10  of https://arxiv.org/pdf/1401.4064.pdf

Webpage reference: http://supernovae.in2p3.fr/sdss_snls_jla/ReadMe.html


TODO: 
 - Start a notebook to read and plot the data from http://supernovae.in2p3.fr/sdss_snls_jla/jla_likelihood_v4.tgz.
 
 The data to be read from file jla_lcparams.txt is mub,X1 and C.  alpha, beta, M* and deltaM in equation 4 (together with 5) are free parameters (called nuisance parameters)
 
 - In the same notebook define the relevant functions to describe such data. As well as the likelihood function according to equation 15 of  https://arxiv.org/pdf/1401.4064.pdf
 
 - Make the MCMC analysis using either emcee or your own code. A first approach is to consider only diagonal covariance matrix we used in the simpler example. I will helpt to update this to use the correct covariance matrix once this is done. 
