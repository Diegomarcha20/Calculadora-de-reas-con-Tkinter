import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  
import math


def calcular_area(event=None): 
    figura = figura_seleccionada.get()
    
    try:
        if figura == "Cuadrado":
            lado = float(entrada_lado.get())
            if lado <= 0:
                raise ValueError("El lado debe ser positivo")
            area = lado * lado
            mostrar_resultado(f"El área del cuadrado es: {area}")
        
        elif figura == "Rectángulo":
            base = float(entrada_base.get())
            altura = float(entrada_altura.get())
            if base <= 0 or altura <= 0:
                raise ValueError("La base y la altura deben ser positivas")
            area = base * altura
            mostrar_resultado(f"El área del rectángulo es: {area}")
        
        elif figura == "Triángulo":
            base = float(entrada_base.get())
            altura = float(entrada_altura.get())
            if base <= 0 or altura <= 0:
                raise ValueError("La base y la altura deben ser positivas")
            area = (base * altura) / 2
            mostrar_resultado(f"El área del triángulo es: {area}")
        
        elif figura == "Círculo":
            radio = float(entrada_radio.get())
            if radio <= 0:
                raise ValueError("El radio debe ser positivo")
            area = math.pi * (radio ** 2)
            mostrar_resultado(f"El área del círculo es: {area:.2f}")
    
    except ValueError as e:
        mostrar_error("¿Cómo vas a hacer eso, gilipichis?")

def mostrar_resultado(mensaje):
    ventana_resultado = tk.Toplevel(ventana)
    ventana_resultado.title("Resultado")
    ventana_resultado.configure(bg="#1E1E2F")
    
    imagen_acertaste = ImageTk.PhotoImage(Image.open("acertaste.png").resize((100, 100)))
    etiqueta_imagen = tk.Label(ventana_resultado, image=imagen_acertaste, bg="#1E1E2F")
    etiqueta_imagen.pack(pady=10)
    
    etiqueta_mensaje = tk.Label(ventana_resultado, text=mensaje, bg="#1E1E2F", fg="white", font=fuente_pixelada)
    etiqueta_mensaje.pack(pady=10)
    
    boton_cerrar = tk.Button(ventana_resultado, text="Cerrar", command=ventana_resultado.destroy, bg="#3E3E5F", fg="white", relief="flat", font=fuente_pixelada)
    boton_cerrar.pack(pady=10)
    
    ventana_resultado.imagen_acertaste = imagen_acertaste
    
    ventana_resultado.update_idletasks()
    ancho = ventana_resultado.winfo_width()
    alto = ventana_resultado.winfo_height()
    ventana_resultado.geometry(f"{ancho}x{alto}")

def mostrar_error(mensaje):
    ventana_error = tk.Toplevel(ventana)
    ventana_error.title("Error")
    ventana_error.configure(bg="#1E1E2F")
    
    imagen_mal = ImageTk.PhotoImage(Image.open("mal.png").resize((100, 100)))
    etiqueta_imagen = tk.Label(ventana_error, image=imagen_mal, bg="#1E1E2F")
    etiqueta_imagen.pack(pady=10)
    

    etiqueta_mensaje = tk.Label(ventana_error, text=mensaje, bg="#1E1E2F", fg="white", font=fuente_pixelada)
    etiqueta_mensaje.pack(pady=10)
    

    boton_cerrar = tk.Button(ventana_error, text="Cerrar", command=ventana_error.destroy, bg="#3E3E5F", fg="white", relief="flat", font=fuente_pixelada)
    boton_cerrar.pack(pady=10)
    
 
    ventana_error.imagen_mal = imagen_mal
    

    ventana_error.update_idletasks()
    ancho = ventana_error.winfo_width()
    alto = ventana_error.winfo_height()
    ventana_error.geometry(f"{ancho}x{alto}")


def mostrar_campos(*args):
    figura = figura_seleccionada.get()
    
  
    etiqueta_lado.grid_remove()
    entrada_lado.grid_remove()
    etiqueta_base.grid_remove()
    entrada_base.grid_remove()
    etiqueta_altura.grid_remove()
    entrada_altura.grid_remove()
    etiqueta_radio.grid_remove()
    entrada_radio.grid_remove()
    
  
    if figura == "Cuadrado":
        imagen_figura.config(image=imagen_cuadrado)
        etiqueta_lado.grid(row=2, column=0, padx=10, pady=5)
        entrada_lado.grid(row=2, column=1, padx=10, pady=5)
        entrada_lado.focus_set()  
        ventana.bind("<Return>", calcular_area)  
    
    elif figura == "Rectángulo":
        imagen_figura.config(image=imagen_rectangulo)
        etiqueta_base.grid(row=2, column=0, padx=10, pady=5)
        entrada_base.grid(row=2, column=1, padx=10, pady=5)
        etiqueta_altura.grid(row=3, column=0, padx=10, pady=5)
        entrada_altura.grid(row=3, column=1, padx=10, pady=5)
        entrada_base.focus_set()  
        ventana.bind("<Return>", calcular_area) 
    
    elif figura == "Triángulo":
        imagen_figura.config(image=imagen_triangulo)
        etiqueta_base.grid(row=2, column=0, padx=10, pady=5)
        entrada_base.grid(row=2, column=1, padx=10, pady=5)
        etiqueta_altura.grid(row=3, column=0, padx=10, pady=5)
        entrada_altura.grid(row=3, column=1, padx=10, pady=5)
        entrada_base.focus_set()  
        ventana.bind("<Return>", calcular_area)  
    
    elif figura == "Círculo":
        imagen_figura.config(image=imagen_circulo)
        etiqueta_radio.grid(row=2, column=0, padx=10, pady=5)
        entrada_radio.grid(row=2, column=1, padx=10, pady=5)
        entrada_radio.focus_set()  
        ventana.bind("<Return>", calcular_area) 
    
   
    ventana.update_idletasks()
    ancho = ventana.winfo_width()
    alto = ventana.winfo_height()
    ventana.geometry(f"{ancho}x{alto}")


ventana = tk.Tk()
ventana.title("Calculadora de Áreas")
ventana.configure(bg="#1E1E2F")  


try:
    
    fuente_pixelada = ("Press Start 2P", 10)
except:
   
    fuente_pixelada = ("Courier", 10)


etiqueta_autor = tk.Label(ventana, text="Hecho por Diego Marciano", font=fuente_pixelada, bg="#1E1E2F", fg="white")
etiqueta_autor.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w")


etiqueta_figura = tk.Label(ventana, text="Seleccione la figura:", bg="#1E1E2F", fg="white", font=fuente_pixelada)
etiqueta_figura.grid(row=1, column=0, padx=10, pady=5)

figuras = ["Cuadrado", "Rectángulo", "Triángulo", "Círculo"]
figura_seleccionada = tk.StringVar(value=figuras[0])
menu_figuras = tk.OptionMenu(ventana, figura_seleccionada, *figuras, command=mostrar_campos)
menu_figuras.config(bg="#3E3E5F", fg="white", relief="flat", bd=0, highlightthickness=0, font=fuente_pixelada)
menu_figuras["menu"].config(bg="#3E3E5F", fg="white", font=fuente_pixelada)
menu_figuras.grid(row=1, column=1, padx=10, pady=5)


imagen_cuadrado = ImageTk.PhotoImage(Image.open("cuadrado.png").resize((100, 100)))
imagen_rectangulo = ImageTk.PhotoImage(Image.open("rectangulo.png").resize((100, 100)))
imagen_triangulo = ImageTk.PhotoImage(Image.open("triangulo.png").resize((100, 100)))
imagen_circulo = ImageTk.PhotoImage(Image.open("circulo.png").resize((100, 100)))


imagen_figura = tk.Label(ventana, bg="#1E1E2F")
imagen_figura.grid(row=5, column=0, columnspan=2, pady=10)


etiqueta_lado = tk.Label(ventana, text="Lado:", bg="#1E1E2F", fg="white", font=fuente_pixelada)
entrada_lado = tk.Entry(ventana, bg="#3E3E5F", fg="white", insertbackground="white", relief="flat", font=fuente_pixelada)

etiqueta_base = tk.Label(ventana, text="Base:", bg="#1E1E2F", fg="white", font=fuente_pixelada)
entrada_base = tk.Entry(ventana, bg="#3E3E5F", fg="white", insertbackground="white", relief="flat", font=fuente_pixelada)

etiqueta_altura = tk.Label(ventana, text="Altura:", bg="#1E1E2F", fg="white", font=fuente_pixelada)
entrada_altura = tk.Entry(ventana, bg="#3E3E5F", fg="white", insertbackground="white", relief="flat", font=fuente_pixelada)

etiqueta_radio = tk.Label(ventana, text="Radio:", bg="#1E1E2F", fg="white", font=fuente_pixelada)
entrada_radio = tk.Entry(ventana, bg="#3E3E5F", fg="white", insertbackground="white", relief="flat", font=fuente_pixelada)


def on_enter(event):
    event.widget.config(bg="#6A5ACD")

def on_leave(event):
    event.widget.config(bg="#3E3E5F")


boton_calcular = tk.Button(ventana, text="Calcular Área", command=calcular_area, bg="#3E3E5F", fg="white", relief="flat", font=fuente_pixelada)
boton_calcular.grid(row=4, column=0, columnspan=2, padx=10, pady=20)
boton_calcular.bind("<Enter>", on_enter)
boton_calcular.bind("<Leave>", on_leave)


ventana.bind("<Return>", calcular_area)


mostrar_campos()


ventana.mainloop()