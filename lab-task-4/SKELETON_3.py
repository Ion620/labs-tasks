import tkinter as tk
import random
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as msg
from tkinter import scrolledtext

# Create instance
win = tk.Tk()

# Add a title
win.title("GUI Python")
# Gets the requested values of the height and widht.
windowWidth = win.winfo_reqwidth()
windowHeight = win.winfo_reqheight()

# Gets both half the screen width/height and window width/height
positionRight = int(win.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(win.winfo_screenheight() / 2 - windowHeight / 2)

# Positions the window in the center of the page.
win.geometry("800x400+{}+{}".format(positionRight, positionDown))

# Disable resizing the GUI by passing in False/False
win.resizable(False, False)

tabControl = ttk.Notebook(win)  # Create Tab Control

# Exit GUI cleanly
def _quit():
    win.quit()
    win.destroy()
    exit()

# Creating a Menu Bar
menu_bar = Menu(win)
win.config(menu=menu_bar)

def laba1():
    """
        Все так як було раніше
    """
    pass

def laba2():
    for id in tabControl.tabs():
        tabControl.forget(id)

    tab1 = ttk.Frame(tabControl)  # Create a tab
    tabControl.add(tab1, text='Завдання 1')  # Add the tab


    tabControl.pack(expand=1, fill="both")  # Pack to make visible

    traffic = ttk.LabelFrame(tab1, text=' Світлофор ')
    traffic.grid(column=0, row=0, padx=8, pady=4)

    def _logger(msg="Hello"):
        pass

    def _popmenu(event, param):
        pass

    logger = ttk.Labelframe(tab1, text="Логовиця")
    logger.grid(column=1, row=0, padx=8, pady=4)
    # Using a scrolled Text control
    scrol_w = 30
    scrol_h = 14
    scrol = scrolledtext.ScrolledText(logger, width=scrol_w, height=scrol_h, wrap=tk.WORD)
    scrol.grid(column=0, row=0, sticky="NESW", columnspan=3)

    remove_control = ttk.LabelFrame(tab1, text=' Пульт ')
    remove_control.grid(column=0, row=1, padx=8, pady=4)

    logger_control = ttk.LabelFrame(tab1, text=' Логовиця ')
    logger_control.grid(column=1, row=1, padx=8, pady=4)

    def _cleaner_scrol():
        pass

    cleaner = ttk.Button(logger_control, text="Очистити", command=_cleaner_scrol)
    cleaner.pack(padx=10, pady=20)
    # First, we change our Radiobutton global variables into a list
    colors = ["Red", "Yellow", "Green"]
    def traffic_lighter(color=None):
        for clr in range(3):
            canvas = tk.Canvas(traffic, width=80, height=80, highlightthickness=1)
            fill_color = colors[clr] if color == colors[clr] else None
            traffic_lighter_color = colors[clr]
            canvas.create_oval(1,1,79,79, fill=fill_color, outline="Black")
            canvas.grid(row=clr, column=4)
            canvas.bind('<Button-1>', lambda event, param={"color": traffic_lighter_color,
                                                           "cur_color": fill_color,
                                                           }: _popmenu(event, param))

    traffic_lighter()
    # We have also changed the callback function to be zero-based, using the list
    # instead of module-level global variables
    # Radiobutton Callback
    def radCall():
        pass

    # create three Radiobuttons using one variable
    radVar = tk.IntVar()

    # Next we are selecting a non-existing index value for radVar
    radVar.set(99)

    # Now we are creating all three Radiobutton widgets within one loop
    for col in range(3):
        curRad = tk.Radiobutton(traffic, text=colors[col], variable=radVar,
                                value=col, command=radCall)
        curRad.grid(column=col, row=1, sticky=tk.W)  # row=6

    # Creating three checkbuttons
    chVar = tk.IntVar()
    check1 = tk.Checkbutton(remove_control, text="Вкл.", variable=chVar)
    check1.select()
    check1.pack(padx=10, pady=20)

    # GUI Callback function
    def checkCallback(*ignoredArgs):
        # only enable one checkbutton
        pass

    chVar.trace('w', lambda unused0, unused1, unused2 : checkCallback())




# Add menu items
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Лаба 1", command=laba1)
file_menu.add_command(label="Лаба 2", command=laba2)
file_menu.add_command(label="Лаба 3", command=laba2)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=_quit)
menu_bar.add_cascade(label="Tasks", menu=file_menu)

# Display a Message Box
def _msgBox():
    msg.showinfo('Python Message Info Box', 'Цей застосунок створено використовуючи tkinter:\nРік стрворення - 2020.\nЯ обожнюю Python ;)')
# Add another Menu to the Menu Bar and an item
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=_msgBox)
menu_bar.add_cascade(label="Help", menu=help_menu)



#======================
# Start GUI
#======================
win.mainloop()