from tkinter import *
from tkinter import ttk

from widgets.constants import ARGUMENTS_LIST, OPTIONS_LIST, DATE_FORMAT_LIST


class Notebook:
    def __init__(self, *args):
        """ Display Notebook section. """
        self.frame = Frame(*args)

        self.notebook = ttk.Notebook(self.frame, padding=(0, 10, 0, 0))
        self.settings = ttk.Frame(self.notebook)
        self.profiles = ttk.Frame(self.notebook)
        self.notebook.add(self.settings, text="Paramètres")
        self.notebook.add(self.profiles, text="Profils")

        # CONSTANTS
        ARGUMENTS = ARGUMENTS_LIST
        OPTIONS = OPTIONS_LIST
        DATE_FORMAT = DATE_FORMAT_LIST

        # --- SETTINGS CONTENT
        self.left_panel = ttk.Frame(self.settings)
        self.left_panel.pack(side=LEFT, fill=X, expand=True)

        # region: Settings
        self.method_labelframe = ttk.LabelFrame(
            self.left_panel, text="Méthode", padding=(0, 5))
        self.method_labelframe.pack(fill=BOTH, pady=4, padx=10)

        # region: Row 01
        self.method_row_01 = ttk.Frame(self.method_labelframe)
        self.method_row_01.pack(anchor=W, fill=X)

        self.lbl_filename = ttk.Label(
            self.method_row_01, text="Nom de fichier :")
        self.lbl_filename.pack(anchor=W, padx=5, fill=X, expand=True)
        self.entry_filename = ttk.Entry(self.method_row_01)
        self.entry_filename.pack(
            anchor=W, side=LEFT, padx=5, fill=X, expand=True)

        self.mb = ttk.Menubutton(self.method_row_01, text="⚙️")
        self.mb.pack()
        self.mb.menu = Menu(self.mb, tearoff=False)
        self.mb["menu"] = self.mb.menu

        for key, value in OPTIONS_LIST.items():
            self.mb.menu.add_command(label=key, command=getattr(
                self, value))
        # endregion: Row 01

        # Row 02
        self.method_row_02 = ttk.Frame(self.method_labelframe)
        self.method_row_02.pack(anchor=W, fill=X, expand=True)

        self.lbl_arguments = ttk.Label(self.method_row_02, text="Arguments :")
        self.lbl_arguments.pack(anchor=W, padx=5)
        self.cbox_arguments = ttk.Combobox(
            self.method_row_02, values=ARGUMENTS, state='readonly')
        self.cbox_arguments.current(0)
        self.cbox_arguments.pack(anchor=W, fill=X, padx=5)
        # endregion: Settings

        # region: Search & Replace
        self.search_labelframe = ttk.LabelFrame(
            self.left_panel, text="Chercher et remplacer", padding=(0, 5))
        self.search_labelframe.pack(fill=BOTH, pady=4, padx=10)

        # Row 01
        self.search_row_01 = ttk.Frame(self.search_labelframe)
        self.search_row_01.pack(anchor=W, fill=X)

        self.lbl_search = ttk.Label(self.search_row_01, text="Recherche :")
        self.lbl_search.pack(anchor=W, padx=5, fill=X, expand=True)
        self.entry_search = ttk.Entry(self.search_row_01)
        self.entry_search.pack(
            anchor=W, side=LEFT, padx=5, fill=X, expand=True)

        # Row 02
        self.search_row_02 = ttk.Frame(self.search_labelframe)
        self.search_row_02.pack(anchor=W, fill=X)

        self.lbl_replace = ttk.Label(self.search_row_02, text="Remplacer :")
        self.lbl_replace.pack(anchor=W, padx=5, fill=X, expand=True)
        self.entry_replace = ttk.Entry(self.search_row_02)
        self.entry_replace.pack(
            anchor=W, side=LEFT, padx=5, fill=X, expand=True)
        # endregion: Search & Replace

        # --- RIGHT PANEL
        self.right_panel = ttk.Frame(self.settings)
        self.right_panel.pack(side=LEFT, fill=BOTH)

        # region: Counter
        self.counter_labelframe = ttk.LabelFrame(
            self.right_panel, text="Compteur", padding=(0, 5))
        self.counter_labelframe.pack(anchor=W, pady=4, padx=10, fill=X)

        self.count_row_01 = ttk.Frame(self.counter_labelframe)
        self.lbl_start = ttk.Label(self.count_row_01, text="Démarrer à :")
        self.lbl_start.pack(anchor=W, side=LEFT)
        self.sbox_start = ttk.Spinbox(
            self.count_row_01, from_=0, to=1000, width=6)
        self.sbox_start.insert(0, 1)
        self.sbox_start.pack(anchor=W, padx=5, side=RIGHT)
        self.count_row_01.pack(fill=X)

        self.count_row_02 = ttk.Frame(self.counter_labelframe)
        self.lbl_step = ttk.Label(self.count_row_02, text="Pas :")
        self.lbl_step.pack(anchor=W, side=LEFT)
        self.sbox_step = ttk.Spinbox(
            self.count_row_02, from_=0, to=100, width=6)
        self.sbox_step.insert(0, 1)
        self.sbox_step.pack(anchor=W, padx=5, side=RIGHT)
        self.count_row_02.pack(fill=X)

        self.count_row_03 = ttk.Frame(self.counter_labelframe)
        self.lbl_nb = ttk.Label(self.count_row_03, text="Nombre de chiffre :")
        self.lbl_nb.pack(side=LEFT)
        self.sbox_nb = ttk.Spinbox(self.count_row_03, from_=0, to=5, width=6)
        self.sbox_nb.insert(0, 2)
        self.sbox_nb.pack(anchor=W, padx=5, side=RIGHT)
        self.count_row_03.pack(fill=X)
        #endregion: Counter

        # region: Date
        self.date_labelframe = ttk.LabelFrame(
            self.right_panel, text="Format date/heure", padding=(0, 5))
        self.date_labelframe.pack(expand=True, fill=X, pady=4, padx=10)

        self.cbox_date = ttk.Combobox(self.date_labelframe, values=DATE_FORMAT)
        self.cbox_date.current(0)
        self.cbox_date.pack(anchor=W, padx=5)
        # endregion: Date

        self.btn_rename = ttk.Button(self.right_panel, text="✔️ Renommer")
        self.btn_rename.pack(pady=12)

        self.check_var = IntVar(value=0)
        self.cbox_rename = ttk.Checkbutton(
            self.right_panel, text="Fermer après renommage.",
            variable=self.check_var, onvalue=1, offvalue=0)
        self.cbox_rename.pack()

        print(self.check_var.get())

        # --- PROFILES CONTENT
        self.lbl_filename = ttk.Label(self.profiles, text="PROFILS")
        self.lbl_filename.pack()

        self.notebook.pack(fill=BOTH, side=TOP)
        self.frame.pack(fill=BOTH)

    @staticmethod
    def option_01():
        print("OPTION 01")

    @staticmethod
    def option_02():
        print("OPTION 02")
