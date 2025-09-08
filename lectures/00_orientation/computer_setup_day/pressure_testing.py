from importlib.metadata import version
import numpy as np

from sklearn.linear_model import LinearRegression

def secret_code():
    z = int(version('numpy').split('.')[0]) 
    z += 10*int(version('pandas').split('.')[0]) 
    z += 100*int(version('matplotlib').split('.')[0])
    z += 1000*int(version('pyjokes').split('.')[1])
    X = np.loadtxt("X.txt", delimiter=",")
    lr = LinearRegression()
    lr.fit(X[:,:2],X[:,2])
    return round(z*lr.coef_.round(2)[0]*lr.coef_.round(2)[1])