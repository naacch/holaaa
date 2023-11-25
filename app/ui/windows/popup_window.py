import tkinter as tk
from tkinter import IntVar,ttk
import customtkinter as ctk

class popup_window(tk.Toplevel):
    def __init__(self,title,width,height):
        super().__init__()
        self.title(title)
        self.geometry(f"{width}x{height}")
        self.resizable(0,0)  

    def form_widgets(self,window_width,window_height,frame_text,df):                             
        frame=tk.LabelFrame(self,text=frame_text)
        frame.place(relheight=0.85,relwidth=1)

        self.canvas=tk.Canvas(frame)
        self.canvas.place(x=0,y=0)

        yscrollbar=tk.Scrollbar(frame,orient="vertical",command=self.canvas.yview)
        yscrollbar.pack(side="right",fill="y")

        self.canvas.configure(yscrollcommand=yscrollbar.set)

        frame2=tk.Frame(self.canvas)
        frame2.config(width=window_width/10*0.85,height=window_height/10*0.85)
        
        self.canvas.create_window((0,0),window=frame2,anchor="nw")
        self.canvas.bind('<Configure>',lambda e:self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.checkboxes_variables={}
        checkboxes={}
        for column in df.columns:
            self.checkboxes_variables[column]=IntVar()
            checkboxes[column]=ctk.CTkCheckBox(self.canvas,
                                               text=column,
                                               text_color="black",
                                               variable=self.checkboxes_variables[column]).pack()
            
    def display_widgets(self):
        frame=tk.LabelFrame(self,text="Peso por variable")
        frame.place(width=500,height=100,x=1,y=1)

        tv=ttk.Treeview(frame)

        xscrollbar=ttk.Scrollbar(frame,
                                 orient="horizontal",
                                 command=tv.xview)
        
        tv.configure(xscrollcommand=xscrollbar.set)
        tv.place(relheight=1, relwidth=1)

        xscrollbar.pack(side="bottom", fill="x")
            
    def acept_button(self):
        button=ctk.CTkButton(self,
                            text="Aceptar",
                            fg_color="grey67",
                            text_color="black")
        return button
    
    def checkboxes_variables_list(self,df):
        list=[]
        for column in df.columns:
            list.append(self.checkboxes_variables[column].get())
        return list
