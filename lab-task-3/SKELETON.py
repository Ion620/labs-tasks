import tkinter as tk
import random
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as msg

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

    remove_control = ttk.LabelFrame(tab1, text=' Пульт ')
    remove_control.grid(column=0, row=1, padx=8, pady=4)
    # First, we change our Radiobutton global variables into a list
    colors = ["Red", "Yellow", "Green"]
    def traffic_lighter(color=None):
        """
        Зробити світлофор, у якого буде підсвічуватися відповідний колір
        """
        pass

    traffic_lighter()

    # Radiobutton Callback
    def radCall():
        radSel = radVar.get()
        if radSel == 0:
            traffic_lighter("Red")
        elif radSel == 1:
            traffic_lighter("Yellow")
        elif radSel == 2:
            traffic_lighter("Green")

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
    check1.grid(column=0, row=4, sticky=tk.W)

    # GUI Callback function
    def checkCallback(*ignoredArgs):
        # only enable one checkbutton
        if chVar.get():
            """
            enable all radiobuttons
            """
            pass
        else:
            """
            disable all radiobuttons
            """
            pass

    chVar.trace('w', lambda unused0, unused1, unused2 : checkCallback())


# Add menu items
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Лаба 1", command=laba1)
file_menu.add_command(label="Лаба 2", command=laba2)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=_quit)
menu_bar.add_cascade(label="Tasks", menu=file_menu)

# Display a Message Box
def _msgBox():
    """
    Створити повідомлення
    """
    pass
# Add another Menu to the Menu Bar and an item
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=_msgBox)
menu_bar.add_cascade(label="Help", menu=help_menu)



#======================
# Start GUI
#======================
win.mainloop()