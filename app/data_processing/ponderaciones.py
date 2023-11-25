import pandas as pd
import numpy as np
from math import log

DECIMALES=3

def critic(df,metodo_corr):
    matriz_corr=df.corr(method=metodo_corr)
    pond=(1-matriz_corr).sum()*df.std()/((1-matriz_corr).sum()*df.std()).sum()
    return pond.round(DECIMALES)

def stdv(df):
    pond=df.std()/df.std().sum()
    return pond.round(DECIMALES)

def entropia(df):
    p=df/df.sum()
    mayorque0=(p>0).all().all()
    if mayorque0==False:
        return "error"
    ayuda=p*np.log(p)
    k=1/log(df.index.size)
    e=-k*ayuda.sum()
    d=1-e
    pond=d/d.sum()
    return pond.round(DECIMALES)

def cv(df):
    cv=df.std()/df.mean()
    return cv/cv.sum()

def igual(df):
    return 1/df.columns.size 

