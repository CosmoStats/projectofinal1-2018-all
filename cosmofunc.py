"""
Funciones utilizadas para el ajuste de los datos del proyecto final.
"""

import numpy as np

def eta(a, omega_m):
    s = s_func(omega_m)
    s2 = s**2.0
    s3 = s**3.0
    s4 = s2**2.0
    coef = [-0.154, 0.4304, 0.19097, 0.066941]
    
    return 2.0 * np.sqrt(s3 + 1.0) * pow(1.0/a**4.0 + coef[0]*s/a**3.0 + coef[1]*s2/a**2.0 + \
           coef[2]*s3/a + coef[3]*s4, -1.0/8.0)

def D_L(z, params):
    H_0 = params[0]
    omega_m = params[1]
    c = 3.0e5 # km/s
    a0 = 1.0
    a1 = 1.0 / (1.0 + z)
    
    return c * (1.0 + z) * (eta(a0, omega_m) - eta(a1, omega_m)) / H_0

def dist_mu(z, params):
    H_0 = params[0]
    
    return 25.0 - 5.0 * np.log10(H_0 / 100.0) + 5.0 * np.log10(D_L(z, params))

def mcmc_step(params_0, params, l0, l1):
    accept_prob = 0.01
    
    if l1 > l0:
        l0 = l1
        params_0 = params
    elif random() < accept_prob:
        l0 = l1
        params_0 = params
    
    return l0, params_0

def walker(Nsamples, params_0,):
    x_sample = []
    y_sample = []
    old_like = log_like(params_0, mu, z, varianza)
    new_like = 0.0
    sigma1 = 1.0 # Para h
    sigma2 = 0.1 # Para omega

    for i in range(Nsamples):
        x_sample.append(params_0[0])
        y_sample.append(params_0[1])
    
        params = [-1.0, -1.0] # h, omega
    
        # Estos ciclos son para moverse cerca de la muestra
        # sin que se salgan del rango.
        while(params[0] < 0 or params[0] > 100):
            params[0] = gauss(params_0[0], sigma1)
        while(params[1] < 0.1 or params[1] > 1.0):
            params[1] = gauss(params_0[1], sigma2)
    
        new_like = log_like(params, mu, z, varianza)
        
        old_like, params_0 = mcmc_step(params_0, params, old_like, new_like)
        
    return x_sample, y_sample

