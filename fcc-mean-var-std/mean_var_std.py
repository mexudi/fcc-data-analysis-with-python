import numpy as np

def calculate(liste):
    if len(liste)!=9:
        raise ValueError("List must contain nine numbers.")
    calculation = {}
    arr = np.array(liste)
    arr = arr.reshape(3,3)
    mean0 = np.mean(arr)
    mean1 = np.mean(arr,axis=0)
    mean2 = np.mean(arr, axis=1)
    calculation['mean'] = [list(mean1), list(mean2),mean0]
    var0 = np.var(arr)
    var1 = np.var(arr, axis=0)
    var2 = np.var(arr, axis=1)
    calculation['variance'] = [list(var1),list(var2),var0]
    std0 = np.std(arr)
    std1 = np.std(arr, axis=0)
    std2 = np.std(arr, axis=1)
    calculation['standard deviation'] = [list(std1), list(std2), std0]
    max0 = np.max(arr)
    max1 = np.max(arr, axis=0)
    max2 = np.max(arr, axis=1)
    calculation['max'] = [list(max1),list(max2),max0]
    min0 = np.min(arr)
    min1 = np.min(arr,axis=0)
    min2 = np.min(arr,axis=1)
    calculation['min'] = [list(min1),list(min2),min0]
    sum0 = np.sum(arr)
    sum1 = np.sum(arr, axis=0)
    sum2 = np.sum(arr,axis=1)
    calculation['sum'] = [list(sum1),list(sum2),sum0]



    return calculation
