import pandas as pd

DECIMALES=3

#polaridad negativa?
def balanceada(df,*args):
    df_estandarizado=pd.DataFrame()
    mediana=df.median()
    min=df.min()
    max=df.max()
    for column in df.columns:
        df_estandarizado[column]=df[column].apply(lambda x: (x - mediana[column])/(mediana[column]-min[column])*30+100 
                                                  if x<=mediana[column] 
                                                  else (x - mediana[column])/(max[column] - mediana[column])*30+100)
    return df_estandarizado.round(DECIMALES)

def clasica(df,polaridad,*args):
    df_estandarizado=pd.DataFrame()
    media=df.mean()
    stdv=df.std(ddof=0)
    for column in df.columns:
        if polaridad[df.columns.get_loc(column)]==0:
            df_estandarizado[column]=df[column].apply(lambda x: (x-media[column])/stdv[column])
        if polaridad[df.columns.get_loc(column)]==1:
            df_estandarizado[column]=df[column].apply(lambda x: 1-(x-media[column])/stdv[column])            
    return df_estandarizado.round(DECIMALES)

def clasica_reescalada(df,polaridad,*args):
    df_estandarizado=pd.DataFrame()
    media=df.mean()
    stdv=df.std(ddof=0)
    for column in df.columns:
        if polaridad[df.columns.get_loc(column)]==0:
            df_estandarizado[column]=df[column].apply(lambda x: 100+(x-media[column])/stdv[column]*10)
        if polaridad[df.columns.get_loc(column)]==1:
            df_estandarizado[column]=df[column].apply(lambda x: 100-(x-media[column])/stdv[column]*10)            
    return df_estandarizado.round(DECIMALES)

def minmax(df,polaridad,rango_min=0,rango_max=1):
    df_estandarizado=pd.DataFrame()
    min=df.min()
    max=df.max()
    print(rango_max,rango_min)
    for column in df.columns:
        if polaridad[df.columns.get_loc(column)]==0:
            df_estandarizado[column]=df[column].apply(lambda x: (x-min[column])/(max[column]-min[column])*(rango_max-rango_min)+rango_min)
        if polaridad[df.columns.get_loc(column)]==1:
            df_estandarizado[column]=df[column].apply(lambda x: (max[column]-x)/(max[column]-min[column])*(rango_max-rango_min)+rango_min)
    return df_estandarizado.round(DECIMALES)

#rango??? 
def minmax_restringida(df,polaridad,*args):
    df_estandarizado=pd.DataFrame()
    min=df.min()
    max=df.max()
    mediana=df.median()
    for column in df.columns:
        if polaridad[df.columns.get_loc(column)]==0:
            df_estandarizado[column]=df[column].apply(lambda x: (x-mediana[column])/(max[column]-min[column]))
        if polaridad[df.columns.get_loc(column)]==1:
            df_estandarizado[column]=df[column].apply(lambda x: (mediana[column]-x)/(max[column]-min[column]))
    return df_estandarizado.round(DECIMALES)

#revisar
def topsis_clasica(df,polaridad,*args):
    df_estandarizado=pd.DataFrame()
    for column in df.columns:
        df_estandarizado[column]=df[column].apply(lambda x: x/pow((df**2)[column].sum(),1/2))
        if polaridad[df.columns.get_loc(column)]==0:
            pis=df.max()
            nis=df.min()
        if polaridad[df.columns.get_loc(column)]==1:
            pis=df.min()
            nis=df.max()            
    return df_estandarizado.round(DECIMALES),pis,nis

#polarizacion??? rango???
def mad(df,polaridad,*args):
    mediana=df.median()
    aux=abs(df-mediana).median()
    df_estandarizado=pd.DataFrame()
    for column in df.columns:
        df_estandarizado[column]=df[column].apply(lambda x: 0.6745*(x-mediana[column])/aux[column])
    return df_estandarizado.round(DECIMALES)

def proporcion(df,polaridad,rango_min,rango_max):
    df_estandarizado=pd.DataFrame()
    for column in df.columns:
        if polaridad[df.columns.get_loc(column)]==0:
            df_estandarizado[column]=df[column]/df.sum()[column]*(rango_max-rango_min)+rango_min
        if polaridad[df.columns.get_loc(column)]==1:
            df_estandarizado[column]=(1-df[column]/df.sum()[column])*(rango_max-rango_min)+rango_min                        
    return df_estandarizado.round(DECIMALES)
    

