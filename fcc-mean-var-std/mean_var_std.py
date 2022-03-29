import numpy as np

def calculate(liste):
    if len(liste)!=9:
        raise ValueError("List must contain nine numbers.")
    calculation = {}
    arr = np.array(liste)
    arr = arr.reshape(3,3)
    calculation['mean'] = [list(np.mean(arr, axis=0), list(np.mean(arr,axis=1),np.mean(arr)]
    calculation['variance'] = [list(np.var(arr,axis=0),list(np.var(arr,axis=1),np.var(arr)]
    calculation['standard deviation'] = [list(np.std(arr,axis=0), list(np.std(arr,axis=1), np.std(arr)]
    calculation['max'] = [list(np.max(arr,axis=0),list(np.max(arr,axis=1),np.max(arr)]
    calculation['min'] = [list(min(np.min(arr,axis=0),list(np.min(arr,axis=1),np.min(arr)]
    calculation['sum'] = [list(np.sum(arr,axis=0),list(np.sum(arr,axis=1),np.sum(arr)]



    return calculation
