from tkinter import *
import tkinter.font as tkFont
import json


class MainScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Chemistry Model")
        self.root.geometry("900x500")
        self.root.resizable(False, False)
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

        # ------------------------------ block of information about the functions ---------------------------
        frame_canvas_information = Frame(main_frame, bg="black")
        frame_canvas_information.grid(row=0, rowspan=2, column=1, sticky='news')
        frame_canvas_information.grid_columnconfigure(0, weight=1)
        frame_canvas_information.grid_rowconfigure(0, weight=1)

        # Set grid_propagate to False to allow the buttons resizing later
        frame_canvas_information.grid_propagate(False)

        # add a canvas
        canvas_information = Canvas(frame_canvas_information, bg="yellow")
        canvas_information.grid(row=0, column=0, sticky="news")

        # link a scrollbar to the canvas
        scrollbar_info = Scrollbar(frame_canvas_information, orient="vertical", command=canvas_information.yview)
        scrollbar_info.grid(row=0, column=1, sticky="ns")
        canvas_information.config(yscrollcommand=scrollbar_info.set)

        # add a frame for content the objects about the functions
        frame_objects_info = Frame(canvas_information, bg="white")
        frame_objects_info.grid_columnconfigure(0, weight=1)
        canvas_information.create_window((0, 0), window=frame_objects_info, anchor='nw')

        # add a label for the title of the function
        fontstyle_label_title_info = tkFont.Font(size=25)
        label_title_information = Label(frame_objects_info, text="Visualizador de moléculas", bg="white",
                                        font=fontstyle_label_title_info, width=32)
        label_title_information.grid(row=0, column=0, sticky='we')

        # add a label for the description of the function
        fontstyle_label_descrip_info = tkFont.Font(size=15)
        label_description_information = Label(frame_objects_info, text="Aquí va una descripcion", bg="white",
                                              font=fontstyle_label_descrip_info, width=30)
        label_description_information.grid(row=1, column=0, sticky="news")

        # add a button for use the function select
        button_use_function = Button(frame_objects_info, text="Usar", bg="white", width=10, height=2)
        button_use_function.grid(row=2, column=0)

        # ------------------------------------- block of functions  --------------------------------------

        fontstyle_func_label = tkFont.Font(size=25)
        label_functions = Label(main_frame, text="Funciones", bg="white", font=fontstyle_func_label)
        label_functions.grid(row=0, column=0, padx=20, pady=(40, 10))

        frame_canvas = Frame(main_frame, bg="black")
        frame_canvas.grid(row=1, column=0, sticky='nw', pady=(30, 60), padx=40)
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

        # define functions for the selector buttons

        varOpcion = IntVar()

        def change_info_description():
            title = ""
            description = ""
            data_description = 'information_of_mainscreen.json'
            with open(data_description, "r") as f_obj:
                data = json.load(f_obj)
                if varOpcion.get() == 1:
                    title += data["title"]["visualizador_moleculas"]
                    description += data["descriptions"]["visualizador_moleculas"]
                    buttons_func[0].deselect()
                elif varOpcion.get() == 2:
                    title += data["title"]["plegamiento"]
                    description += data["descriptions"]["plegamiento"]
                    buttons_func[1].deselect()
                elif varOpcion.get() == 3:
                    title += data["title"]["alineamiento"]
                    description += data["descriptions"]["alineamiento"]
                    buttons_func[2].deselect()
                elif varOpcion.get() == 4:
                    title += data["title"]["grafica_sesgo"]
                    description += data["descriptions"]["grafica_sesgo"]
                    buttons_func[3].deselect()
                elif varOpcion.get() == 5:
                    title += data["title"]["identificar_colonias"]
                    description += data["descriptions"]["identificar_colonias"]
                    buttons_func[4].deselect()
                else:
                    pass
            label_title_information.config(text=title)
            label_description_information.config(text=description)

        num_buttons = 5
        buttons_func = [Radiobutton() for i in range(num_buttons)]
        buttons_func[0] = Radiobutton(frame_buttons_func, text="Visualizador de moleculas", width=25, height=4,
                                      variable=varOpcion, value=1, command=change_info_description,
                                      indicatoron=0)
        buttons_func[0].grid(row=0, column=0, sticky='news')
        buttons_func[1] = Radiobutton(frame_buttons_func, text="Frecuencia de nucleotidos", width=25, height=4,
                                      variable=varOpcion, value=2, command=change_info_description,
                                      indicatoron=0)
        buttons_func[1].grid(row=1, column=0, sticky='news')
        buttons_func[2] = Radiobutton(frame_buttons_func, text="Alineamiento de proteínas", width=25, height=4,
                                      variable=varOpcion, value=3, command=change_info_description,
                                      indicatoron=0)
        buttons_func[2].grid(row=2, column=0, sticky='news')
        buttons_func[3] = Radiobutton(frame_buttons_func, text="Plegamiento de proteínas", width=25, height=4,
                                      variable=varOpcion, value=4, command=change_info_description,
                                      indicatoron=0)
        buttons_func[3].grid(row=3, column=0, sticky='news')
        buttons_func[4] = Radiobutton(frame_buttons_func, text="Identificador de colonias", width=25, height=4,
                                      variable=varOpcion, value=5, command=change_info_description,
                                      indicatoron=0)
        buttons_func[4].grid(row=4, column=0, sticky='news')
        # buttons_func[5] = Button(frame_buttons_func, text="Árboles genealogicos", width=25, height=4)
        # buttons_func[5].grid(row=5, column=0, sticky='news')

        # update buttons frames idle task to let tkinter calculate buttons sizes
        frame_buttons_func.update_idletasks()

        frame_canvas.config(width=200, height=400)

        # define the area of the scrollbar
        canvas_func.config(scrollregion=canvas_func.bbox("all"))

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
