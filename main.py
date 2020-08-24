from tkinter import *

# diseño principal de la primer ventana
root = Tk()
root.title("Chemistry Model")
root.resizable(True, True)
root.geometry("800x500")
root.config(bg="white")

# diseño de barra menu
barraMenu = Menu(root)
root.config(menu=barraMenu)

# diseño de la barra de menu
archivoMenu = Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir")
barraMenu.add_cascade(label="Archivo", menu=archivoMenu)

ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Chemistry Model tutorial")
ayudaMenu.add_command(label="Perfil de Github")
ayudaMenu.add_command(label="Acerca de Chemistry Model")
ayudaMenu.add_separator()
ayudaMenu.add_command(label="Comentarios")
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

# diseño de la parte central
frame_main = Frame(root, width=800, height=500, bg="white")
frame_main.pack()

funcionesLabel = Label(frame_main, text="Funciones")
funcionesLabel.grid(row=0, column=0, padx=20, pady=10)

funcionesOpcionesLabel = Label(frame_main)







root.mainloop()
