import tkinter as tk
from tkinter import ttk,StringVar
import customtkinter as ctk
from app.logic.app_controller import *

class main_window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("")
        self.geometry("1400x800")
        self.resizable(0,0)
        self.widgets()
    
    def widgets(self):
        frame_tv=tk.Frame(self)
        frame_tv.place(height=600, width=1350, x=25,y=25)

        style=ttk.Style()
        style.theme_use("default")
        style.configure("treeview",
                        background="grey90",
                        foreground="black",
                        fieldbackground="grey90")
        style.map("treeview",
                  background=[("selected","skyblue2")])
        
        tv_principal=ttk.Treeview(frame_tv)
        tv_principal.pack(fill="both",expand=True)
        xscrollbar_tv_principal=tk.Scrollbar(tv_principal, orient="horizontal", command=tv_principal.xview)
        xscrollbar_tv_principal.pack(fill="x",side="bottom")
        yscrollbar_tv_principal=tk.Scrollbar(tv_principal,orient="vertical",command=tv_principal.yview)
        yscrollbar_tv_principal.pack(fill="y",side="right")

        frame_botones_principal=tk.LabelFrame(self,text="")
        frame_botones_principal.place(height=150,width=190,x=25,y=635)

        frame_botones_secundario=tk.Frame(frame_botones_principal)
        frame_botones_secundario.place(height=110,relx=0.5,rely=0.5,anchor="center")

        boton_abrir_archivo=ctk.CTkButton(frame_botones_secundario,
                                          text="Abrir archivo Excel",
                                          fg_color="grey67",
                                          text_color="black",
                                          height=50,
                                          command=lambda: read_and_display_df(tv_principal))
        boton_abrir_archivo.pack(side="top")

        boton_exportar_archivo=ctk.CTkButton(frame_botones_secundario,
                                             text="Exportar archivo Excel",
                                             fg_color="grey67",
                                             text_color="black",
                                             height=50)
        boton_exportar_archivo.pack(side="bottom")
        boton_polarizacion=ctk.CTkButton(self,
                                         text="Polarización",
                                         fg_color="grey67",
                                         text_color="black",
                                         command=lambda: polarity_window(tv_principal))
        boton_polarizacion.place(x=240,y=645)

        frame_estandarizacion_principal=tk.LabelFrame(self,
                                            text="Selecciona el tipo de estandarización que desea realizar")
        frame_estandarizacion_principal.place(height=100,width=310,x=240,y=685)

        frame_estandarizacion_secundario=tk.Frame(frame_estandarizacion_principal)
        frame_estandarizacion_secundario.place(height=70,relx=0.5,rely=0.5,anchor="center")

        boton_aceptar_estandarizacion=ctk.CTkButton(frame_estandarizacion_secundario,
                                                    text="Aceptar",
                                                    fg_color="grey67",
                                                    text_color="black")
        boton_aceptar_estandarizacion.pack(side="bottom")

        estandarizacion_clicked=StringVar(value="Estandarizaciones")
        optionmenu_estandarizacion=ctk.CTkOptionMenu(frame_estandarizacion_secundario,
                                                     width=140,
                                                     values=list(ESTANDARIZACIONES.keys()),
                                                     variable=estandarizacion_clicked,
                                                     command=lambda event: chosen_standardization(estandarizacion_clicked.get(),
                                                                                                  boton_aceptar_estandarizacion,
                                                                                                  tv_principal,
                                                                                                  entry_rangomin,
                                                                                                  entry_rangomax,
                                                                                                  boton_aceptar_rango))
        optionmenu_estandarizacion.pack(side="top")

        frame_rango=tk.LabelFrame(self,
                                  text="Seleccione el rango que desea utilizar en la estandarizacion")
        frame_rango.place(height=150,width=350,x=575,y=635)

        label_rangomax=ctk.CTkLabel(frame_rango,
                                    text="Valor maximo",
                                    text_color="black")
        label_rangomax.place(x=190,y=7)

        label_rangomin=ctk.CTkLabel(frame_rango,
                                    text="Valor minimo",
                                    text_color="black")
        label_rangomin.place(x=15,y=7)

        entry_rangomax=ctk.CTkEntry(frame_rango,
                                    fg_color="grey87",
                                    border_color="grey87",
                                    text_color="black")
        entry_rangomax.place(x=190,y=37)

        entry_rangomin=ctk.CTkEntry(frame_rango,
                                    fg_color="grey87",
                                    border_color="grey87",
                                    text_color="black")
        entry_rangomin.place(x=15,y=37)

        boton_aceptar_rango=ctk.CTkButton(frame_rango,
                                          text="Aceptar",
                                          fg_color="grey67",
                                          text_color="black")
        boton_aceptar_rango.place(x=97,y=85)

        frame_ponderacion_principal=tk.LabelFrame(self,
                                                  text="Seleccione el tipo de ponderación")
        frame_ponderacion_principal.place(height=150,width=200,x=950,y=635)

        frame_ponderacion_secundario=tk.Frame(frame_ponderacion_principal)
        frame_ponderacion_secundario.place(height=70,relx=0.5,rely=0.5,anchor="center")
        
        ponderacion_clicked=StringVar(value="Ponderaciones")
        optionmenu_ponderacion=ctk.CTkOptionMenu(frame_ponderacion_secundario,
                                                 width=140,
                                                 values=list(PONDERACIONES.keys()),
                                                 variable=ponderacion_clicked)
        optionmenu_ponderacion.pack(side="top")

        boton_aceptar_ponderacion=ctk.CTkButton(frame_ponderacion_secundario,
                                                text="Aceptar",
                                                fg_color="grey67",
                                                text_color="black")
        boton_aceptar_ponderacion.pack(side="bottom")

        frame_agregacion_principal=tk.LabelFrame(self,
                                                 text="Seleccione el tipo de agregación")
        frame_agregacion_principal.place(height=150,width=200,x=1175,y=635)

        frame_agregacion_secundario=tk.Label(frame_agregacion_principal)
        frame_agregacion_secundario.place(height=80,relx=0.5,rely=0.5,anchor="center")

        optionmenu_agregacion=ctk.CTkOptionMenu(frame_agregacion_secundario,
                                                width=140,
                                                values=AGREGACIONES).pack(side="top")

        boton_aceptar_agregacion=ctk.CTkButton(frame_agregacion_secundario,
                                               text="Aceptar",
                                               fg_color="grey67",
                                               text_color="black").pack(side="bottom")
