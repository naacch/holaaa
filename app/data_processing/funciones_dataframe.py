from tkinter import filedialog
import pandas as pd

def read_df(): 
    filename=filedialog.askopenfilename(initialdir="/",
                                        title='Seleccionar archivo',
                                        filetypes=[("excel file", "*.xlsx")])
    #solo lee archivos .xlsx
    df=pd.read_excel(filename)
    df=df.set_index(df.iloc[:,0]).drop(df.columns[0],axis=1)
    return df

def clean_tv(tv):
    tv.delete(*tv.get_children())

def display_df_data(df,tv,show_index=True):
    #muestra los datos de un dataframe en un treeview
    clean_tv(tv)
    
    columns=list(df.columns)
    if show_index==True:
        columns.insert(0,"index")
        for index, row in df.iterrows():
            tv.insert("", "end", values=([index] + list(row)))
    elif show_index==False:
        for index,row in df.iterrows():
            tv.insert("", "end", values=list(row))
    
    return columns 

def display_df_headings(tv,columns):
    #muestra los encabezados de un dataframe
    tv["column"] = columns
    tv["show"] = "headings"
    for column in tv["columns"]:
         tv.heading(column, text=column)

def display_complete_df(df,tv,show_index=True):
    columns=display_df_data(df,tv,show_index)
    display_df_headings(tv,columns)