# Consider having a main menu that allows download of flex report XML
# then select XL reports to create and select launching ATF_menu

# - - For the GUI - - - - - - - - - - - - - - - - - - - - - - - - - - - -
import tkinter as tk
from tkinter import Tk, IntVar, Frame, Label
from tkinter import ttk
from PIL import Image, ImageTk

# Import modules 
import datetime as dt

# - - For report parameters
import code.file as file     # module to read json file

# - - Main app class - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class AI_Main():
    def __init__(self):
        self.root = tk.Tk()
        self.root.rowconfigure(1, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.title("Open AI Main Menu")
        # Creates a logo for the window
        self.root.iconbitmap(default="images/openai-logomark.ico")
        self.root.geometry('{}x{}'.format(800, 300))
        # Call functions to buidl rest of UI
        self.create_frames()

# - - Functions go here
    def dlXMLclick(self):
        self.dlXML_button["text"] = "Processing"
        print("downloading")
        import code.ai_script
        self.dlXML_button["text"] = "Created"

    def create_frames(self):
# - - The Commands frame (connect / disconnect with IB) - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        self.cmd_frame = ttk.LabelFrame(self.root, text="AI Processing", relief=tk.RIDGE)
        self.cmd_frame.grid(row=0, column=0, columnspan = 4,sticky="news", padx=(0,5), ipadx=5)
        self.cmd_frame.rowconfigure(1, weight=1)
        self.cmd_frame.columnconfigure(1, weight=1)

        # Create a label with IB Logo for Command Frame
        image1 = Image.open('images/OpenAI_sm.png')
        atf_logo = ImageTk.PhotoImage(image1)
        self.label1 = ttk.Label(self.cmd_frame, image=atf_logo)
        self.label1.image = atf_logo
        self.label1.grid(row=0, column=0, sticky=tk.W, pady=3)
        self.label2 = ttk.Label(self.root, text='OpenAI processing')
        self.label2.grid(row=1, column=0, sticky=tk.W, padx=(10,10))
        self.dlXML_button = ttk.Button(self.root, text="Generate Content", command=self.dlXMLclick)
        self.dlXML_button.grid(row=1, column=1, sticky=tk.W, padx=(10,5))
        self.label3 = ttk.Label(self.root, text='')
        self.label3.grid(row=1, column=1, sticky=tk.E, padx=(10,10))



# - - The Bottom Status frame - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        self.stat_frame = ttk.LabelFrame(self.root, text="Status", relief=tk.RIDGE)
        self.stat_frame.grid(row=3, column=0, columnspan = 4,sticky="ews", padx=(0,5), ipadx=5)
        self.stat_frame.rowconfigure(1, weight=1)
        self.stat_frame.columnconfigure(1, weight=1)

    # - - Quit button in the lower right corner - - - - - - - - - - - - - - - - - - - - - - -
        self.quit_button = ttk.Button(self.root, text="Quit", command=self.root.destroy)
        self.quit_button.grid(row=4, column=3, sticky=tk.E)

# Create the entire GUI app
app = AI_Main()

# Start the GUI event loop
app.root.mainloop()