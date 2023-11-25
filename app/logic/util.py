import time
from tkinter import END

def execution_time(function,*args):
    start=time.time()
    function(*args)
    end=time.time()
    print(end-start)

def value_in_dict(dict,key):
    value=dict.get(key,None)
    return value is not None

def change_button_function(button,function,*args):
    button.configure(command=lambda:function(*args))
    
def entry_fixed_value(entry,value):
    delete_entry_value(entry)
    entry.insert(0,value)
    entry.configure(state="disabled")

def delete_entry_value(entry):
    entry.configure(state="normal")
    entry.delete(0,END)

def change_heading_text(tv,column,text):
    tv.heading(f"#{column+2}",text=text)

def assign_dict_value(dict,key,value):
    dict[key]=value
