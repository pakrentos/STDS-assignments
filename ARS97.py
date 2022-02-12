import numpy as np

def ARS97(fname, n, q):
    m = 2**12
    r = n//m
    s = 2**9
    alpha = q*n

    samples = []
    f = open(fname, 'rb')
    for par_ind in range(r):
        par = np.fromfile(f, count=m, dtype='float32')
        par = np.sort(par, kind='heapsort').reshape(s, -1).max(-1)
        samples.append(par)
    f.close()
    samples = np.concatenate(samples)
    samples = np.sort(samples, kind='heapsort')

    l_ind = np.floor(s/m*alpha - (r - 1)*(1 - s/m))
    l_ind = int(l_ind)
    u_ind = np.ceil(alpha*s/m)
    u_ind = int(u_ind)
    return samples[l_ind], samples[u_ind]