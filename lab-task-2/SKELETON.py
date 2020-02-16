import tkinter as tk
import random
from tkinter import ttk
from tkinter import Menu
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
win.geometry("500x300+{}+{}".format(positionRight, positionDown))

# Disable resizing the GUI by passing in False/False
win.resizable(False, False)

# Exit GUI cleanly
def _quit():
    win.quit()
    win.destroy()
    exit()

# Creating a Menu Bar
menu_bar = Menu(win)
win.config(menu=menu_bar)

def laba1():
    tabControl = ttk.Notebook(win)  # Create Tab Control

    tab1 = ttk.Frame(tabControl)  # Create a tab
    tabControl.add(tab1, text='Завдання 1')  # Add the tab
    tab2 = ttk.Frame(tabControl)  # Add a second tab
    tabControl.add(tab2, text='Завдання 2')  # Make second tab visible

    tab3 = ttk.Frame(tabControl)  # Add a second tab
    tabControl.add(tab3, text='Завдання 3')  # Make second tab visible

    tab4 = ttk.Frame(tabControl)  # Add a second tab
    tabControl.add(tab4, text='Завдання 4')  # Make second tab visible


    tabControl.pack(expand=1, fill="both")  # Pack to make visible


# Add menu items
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Лаба 1", command=laba1)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=_quit)
menu_bar.add_cascade(label="Tasks", menu=file_menu)

# Add another Menu to the Menu Bar and an item
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About")
menu_bar.add_cascade(label="Help", menu=help_menu)



#======================
# Start GUI
#======================
win.mainloop()