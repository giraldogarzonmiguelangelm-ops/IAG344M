#https://docs.python.org/es/3/library/tkinter.html
import tkinter as tk
from tkinter import filedialog,messagebox #Nos da la posibiliodad de manejar dialogos de archivo y cajas de mensaje
from proccessor import process_excel_safe
#Nos permite seleccionar el archivo de Excel y cargarlo
def seleccionar_excel():
    return filedialog.askopenfilename(   
    title = "Seleccionar archivo de Excel",
    filetypes=[("Archivo Excel","*.xlsx")]
    )
#Recibe el archivo seleccionado en la variable archivo
def on_clic_procesar():
    archivo = seleccionar_excel()
    exito,mensaje = process_excel_safe(archivo)
    if exito:
        messagebox.showinfo("Proceso completado", mensaje)
    else:
        messagebox.showerror("Error", mensaje)

def iniciar_app():
    root = tk.Tk()
    root.title("Procesador de archivos Excel")
    root.geometry("400x400")
    root.resizable(False,False)

    boton = tk.Button(
        root ,
        text="Seleccionar archivo excel",
        command = on_clic_procesar,
        width=30,
        height=2
    )
    boton.pack(pady=60)
    root.mainloop()