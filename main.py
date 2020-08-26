from tkinter import *
import tkinter.font as tkFont


class MainScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Chemistry Model")
        self.root.geometry("900x500")
        self.root.resizable(True, True)
        self.root.config(bg="white")
        # design of main frame
        self.mainFrame()
        # design of main menu
        self.mainMenu()

    def mainFrame(self):
        main_frame = Frame(self.root, bg="white")
        main_frame.pack(fill=BOTH, expand=True)

        main_frame.columnconfigure(0, weight=0)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=7)

        fontstyle_func_label = tkFont.Font(size=25)
        funciones_label = Label(main_frame, text="Funciones", bg="white", font=fontstyle_func_label)
        funciones_label.grid(row=0, column=0, padx=20, pady=(40, 10))

        frame_canvas = Frame(main_frame, bg="black")
        frame_canvas.grid(row=1, column=0, sticky='news', pady=(30, 60), padx=40)
        frame_canvas.grid_rowconfigure(0, weight=1)
        frame_canvas.grid_columnconfigure(0, weight=1)

        # Set grid_propagate to False to allow the buttons resizing later
        frame_canvas.grid_propagate(False)

        # add a canvas
        canvas_func = Canvas(frame_canvas, bg="yellow")
        canvas_func.grid(row=0, column=0, sticky='news')

        # Link a scrollbar to the canvas
        scrollbar_func = Scrollbar(frame_canvas, orient="vertical", command=canvas_func.yview)
        scrollbar_func.grid(row=0, column=1, sticky='ns')
        canvas_func.config(yscrollcommand=scrollbar_func.set)

        # Add a frame for contain the buttons
        frame_buttons_func = Frame(canvas_func, bg="blue")
        frame_buttons_func.grid_columnconfigure(0, weight=1)
        canvas_func.create_window((0, 0), window=frame_buttons_func, anchor='nw')

        num_buttons = 6
        buttons_func = [Button() for i in range(num_buttons)]
        buttons_func[0] = Button(frame_buttons_func, text="Visualizador de moleculas", width=25, height=4)
        buttons_func[0].grid(row=0, column=0, sticky='news')
        buttons_func[1] = Button(frame_buttons_func, text="Frecuencia de nucleotidos", width=25, height=4)
        buttons_func[1].grid(row=1, column=0, sticky='news')
        buttons_func[2] = Button(frame_buttons_func, text="Alineamiento de proteínas", width=25, height=4)
        buttons_func[2].grid(row=2, column=0, sticky='news')
        buttons_func[3] = Button(frame_buttons_func, text="Plegamiento de proteínas", width=25, height=4)
        buttons_func[3].grid(row=3, column=0, sticky='news')
        buttons_func[4] = Button(frame_buttons_func, text="Arboles genealogicos", width=25, height=4)
        buttons_func[4].grid(row=4, column=0, sticky='news')
        buttons_func[5] = Button(frame_buttons_func, text="Identificador de colonias", width=25, height=4)
        buttons_func[5].grid(row=5, column=0, sticky='news')

        frame_buttons_func.update_idletasks()

        frame_canvas.config(width=200, height=400)

        # define the area of the scrollbar
        canvas_func.config(scrollregion=canvas_func.bbox("all"))

        frame_information = Frame(main_frame, bg="black")
        frame_information.grid(row=0, rowspan=2, column=1, sticky='news')

    def mainMenu(self):
        bar_menu = Menu(self.root)
        self.root.config(menu=bar_menu)

        archivoMenu = Menu(bar_menu, tearoff=0)
        archivoMenu.add_command(label="Nuevo")
        archivoMenu.add_separator()
        archivoMenu.add_command(label="Salir")
        bar_menu.add_cascade(label="Archivo", menu=archivoMenu)

        ayudaMenu = Menu(bar_menu, tearoff=0)
        ayudaMenu.add_command(label="Chemistry Model tutorial")
        ayudaMenu.add_command(label="Perfil de Github")
        ayudaMenu.add_command(label="Acerca de Chemistry Model")
        ayudaMenu.add_separator()
        ayudaMenu.add_command(label="Comentarios")
        bar_menu.add_cascade(label="Ayuda", menu=ayudaMenu)


def main():
    root = Tk()
    app = MainScreen(root)
    root.mainloop()


if __name__ == '__main__':
    main()
