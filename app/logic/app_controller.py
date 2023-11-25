from app.data_processing.estandarizaciones import *
from app.data_processing.funciones_dataframe import *
from app.logic.util import *
from app.data_processing.ponderaciones import *
from app.logic.error import *
from app.ui.windows.popup_window import popup_window

data={"raw":None,
      "standardized":None,
      "polarity":None}

ESTANDARIZACIONES={"Balanceada":balanceada,
                   "Clasica":clasica,
                   "Clasica reescalada 90-110":clasica_reescalada,
                   "Clasica restringida":None,
                   "MAD":mad,
                   "Min-max clasica":minmax,
                   "Min-max reescalada":minmax,
                   "Min-max restringida": minmax_restringida,
                   "TOPSIS clasica":topsis_clasica}

FIXED_RANGE={"Balanceada":[70,130],
             "Clasica":["",""],
             "Clasica reescalada 90-110":[90,110],
             "MAD":["",""],
             "Min-max clasica":[0,1]}

PONDERACIONES={"Coeficiente de variacion":cv,
               "CRITIC":critic,
               "Entropia":entropia,
               "Stdv":stdv}

AGREGACIONES=[]

WIDGETS_POPUPS_WINDOWS={"polarity":popup_window.form_widgets}

POLARITY_WINDOW={"title":"Polaridad",
                 "width":350,
                 "height":355,
                 "frame text":"Seleccione las variables con polaridad negativa",
                 "data":data["raw"]}

def read_and_display_df(tv):
    data["raw"]=read_df()
    execution_time(display_complete_df,data["raw"],tv)

def calculate_and_display_df(operations_dict,operations_key,data_key,tv,*args): 
    #data_key es la clave del diccionario data
    function=operations_dict.get(operations_key,None)
    data[data_key]=function(*args)
    display_df_data(data[data_key],tv)

def get_range(entry_min_range,entry_max_range):
    data["range"]=[entry_min_range.get(),entry_max_range.get()]

def disabled_entrys_and_button(entry_min_range,entry_max_range,fixed_range,button):#cambiar nombre
    #fixed_range es una lista que contiene el rango minimo y el rango max [min_range,max_range]
    entry_fixed_value(entry_min_range,fixed_range[0])
    entry_fixed_value(entry_max_range,fixed_range[1])
    button.configure(state="disabled")

def chosen_standardization(chosen_option,button_standardization,tv,entry_min_range,entry_max_range,button_range):
    if value_in_dict(FIXED_RANGE,chosen_option)==True: #si la estandarizacion tiene un rango preestablecido usa ese rango
        data["range"]=FIXED_RANGE.get(chosen_option,None)
        disabled_entrys_and_button(entry_min_range,entry_max_range,data["range"],button_range)
    elif value_in_dict(FIXED_RANGE,chosen_option)==False:
        delete_entry_value(entry_min_range)
        delete_entry_value(entry_max_range)
        button_range.configure(state="normal")

    change_button_function(button_standardization,calculate_and_display_df,
                           ESTANDARIZACIONES,chosen_option,"standardized",tv,
                           data["raw"],data["polarity"],data["range"][0],data["range"][1])    
    #esta funcion para este caso especifico utiliza 10 parametros
    #4 de ellos son parametros de la estandarizacion
    #como lo cambiooo?????
    
def create_popup_window(widgets_popups_windows_key,dict_window,df):
    window=popup_window(dict_window["title"],
                        dict_window["width"],
                        dict_window["height"])
    
    WIDGETS_POPUPS_WINDOWS[widgets_popups_windows_key](window,
                                                       dict_window["width"],
                                                       dict_window["height"],
                                                       dict_window["frame text"],
                                                       df)
    
    button=window.acept_button()

    return window,button

def polarity_window(tv):
    window,button=create_popup_window("polarity",POLARITY_WINDOW,data["raw"])
    
    def button_function():
        data["polarity"]=window.checkboxes_variables_list(data["raw"])
        window.destroy()
        for column in data["raw"]: 
            position=data["raw"].columns.get_loc(column)
            if data["polarity"][position]==0:
                change_heading_text(tv,position,f"{column} (+)")
            elif data["polarity"][position]==1:
                change_heading_text(tv,position,f"{column} (-)")

    button.pack(side="bottom")
    button.configure(command=button_function)