import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Ventana Simple")

## Funciones después de los import
def mostrar_mensaje():
    messagebox.showinfo("Aviso", "Botón Presionado!!")

label = tk.label(ventana, text="Presiona el botón para ver un mensaje")
label.pack(pady=10)

boton = tk.button(ventana, text= "haz click aqui", command=mostrar_mensaje)
boton.pack(pady=10)

ventana.mainloop() ## Mainloop siempre va al final y es solo UNO