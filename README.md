## Proyecto de detector de spam
Esto fue un detector de spam guiado y hecho por lo maestros, hice un detector funcional con 5575 lineas de frases que sean posiblemente SPAM o NO SPAM y basicamente nos ayuda a entender un poco mas como funciona tkinter 
## como?
primero fue crear una carpeta en la que guardaramos nuestras lineas de codigo 
despues fue hacer una cuenta de gifhub donde podramos guardar nuestro codigo como almacenamiento digital
para eso descargamos git bash para poder vinclar nuestro visual studio con nuestra cuenta de gifhub
pero tenemos que tener instalad-o .pip en nuestra cmd
verificamos se haya instalado
en la cmd abrimos el git bash
vinculamos la cuenta de gifhub en la terminal que se abre
abrimos visual studio con la cmd
copeamos el codigo que proyectaron y explicaron en la clase en cada script determinado
agregamos otra carpeta llamada "venv"
en venv agregamos la ,gitgnore que son cosas que vamos a ignorar
agregamos otra que venga con la licencia del detector de spam que usamos 
y por ultimo escribi la tarea en el script README.md
## cosas a futuro
seguir viendo tutoriales en youtube de como hacer cosas con python como animaciones como esta que me gusto y desde ahi empece a ver mas tutoriales de que mas se puede hacer con python y la biblioteca de tkinter

from tkinter import Canvas, Tk, Frame
from math import sin, cos, pow
from random import randint, choice

class Heart(Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.canvas = Canvas(master, bg="black")
        self.canvas.place(relx=0, rely=0, relwidth=1, relheight=1)   
            
        self.objects = []  
        self.num = 0
        self.chars = ["✶", "☆", "✿", "★", "❀", "๑ï", "➴", "♡"]
        self.char = "✶"
        
        self.create_obj()
        self.update()
        
    def create_obj(self):
        for i in range(200):
            obj = self.canvas.create_text(0, 0, font=("Arial", 24))
            self.canvas.coords(obj, 500, 250)
            self.objects.append(obj)
            
    def draw(self, obj, x, y, color, char):
        self.canvas.itemconfig(obj, fill=color, text=char)
        self.canvas.move(obj, x, y)
    
    def update(self):
        for t in range(0, 200, 1):
            xp = -1 * int(16 * pow(sin(t), 3))
            yp = -1 * int(13 * cos(t) - 5 * cos(2*t) - 2 * cos(3*t) - cos(4*t))
            color = "#{:02x}{:02x}{:02x}".format(randint(100, 255), 0, randint(100, 255))
            
            self.draw(self.objects[self.num], xp, yp, color, self.char)
            
            xy = self.canvas.coords(self.objects[self.num])
            
            self.num += 1
            if self.num >= 200:
                self.num = 0
            if xy[0] >= 800:
                self.char = choice(self.chars)
                for s in range(200):
                    self.canvas.moveto(self.objects[s], 520, 270)
        
        self.master.after(100, self.update)
                  
if __name__ == "__main__":
    root = Tk()
    root.title("Feliz Cumpleaños Gatita Llorona ♡")
    root.geometry("1200x700")
    import os
root.iconbitmap(os.path.join(os.path.dirname(__file__), "Mena.ico")) ## elimine esto
app = Heart(root)
app.mainloop()

