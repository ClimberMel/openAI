"""A GUI to send and recieve requests and responses from OpenAI ChatGPT"""

# - - For the GUI - - - - - - - - - - - - - - - - - - - - - - - - - - - -
import tkinter as tk
from tkinter import Tk, IntVar, Frame, Label
from tkinter import ttk
import tkinter.scrolledtext as st
from PIL import Image, ImageTk

# Import modules 
import datetime as dt
import code.ai_script as ai         # - - The processing code
import code.file as file            # - - For reading parameters

# - - Main app class - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class AI_Main():
    def __init__(self):
        self.root = tk.Tk()
        self.root.rowconfigure(1, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.title("Open AI Main Menu")
        # Creates a icon for the main window
        self.root.iconbitmap(default="images/openai-logomark.ico")
        self.root.geometry('{}x{}'.format(800, 500))
        # Call functions to buidl rest of UI
        self.create_frames()

# - - Functions go here
    def dlXMLclick(self):
        self.dlXML_button["text"] = "Processing"
        prompt = self.inputtxt.get(1.0, "end-1c")        
        if prompt == "":                                    # prevents trying to get a response if request is blank
            self.response.delete("1.0",tk.END)
            self.response.insert(tk.INSERT, "Please enter a request above!")
        else:
            self.dlXML_button["text"] = "Created"
            self.response.delete("1.0",tk.END)
            responseText = ai.chat_gpt(prompt)
            self.response.insert(tk.INSERT, responseText)

    def create_frames(self):
    # - - The Header frame - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        self.hdr_frame = ttk.LabelFrame(self.root, text="AI Processing", relief=tk.RIDGE)
        self.hdr_frame.grid(row=0, column=0, columnspan = 4,sticky="news", padx=(0,5), ipadx=5)
        self.hdr_frame.rowconfigure(1, weight=1)
        self.hdr_frame.columnconfigure(1, weight=1)
        # logo
        image1 = Image.open('images/OpenAI_sm.png')
        atf_logo = ImageTk.PhotoImage(image1)
        self.label1 = ttk.Label(self.hdr_frame, image=atf_logo)
        self.label1.image = atf_logo
        self.label1.grid(row=0, column=0, sticky=tk.W, pady=3)        
        # in root frame
        self.label2 = ttk.Label(self.root, text='Input your request: ')
        self.label2.grid(row=1, column=0, sticky=tk.NW, padx=(10,10))
        self.inputtxt = tk.Text(self.root, 
                    height = 5, 
                    width = 60) 
        self.inputtxt.grid(row=1, column=1, sticky=tk.NW, padx=(10,10))        
        self.label3 = ttk.Label(self.root, text='OpenAI processing')
        self.label3.grid(row=2, column=0, sticky=tk.W, padx=(10,10))
        self.dlXML_button = ttk.Button(self.root, text="Generate Content", command=self.dlXMLclick)
        self.dlXML_button.grid(row=2, column=1, sticky=tk.W, padx=(10,5))
    # - - The Bottom Status / Response frame - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        self.stat_frame = ttk.LabelFrame(self.root, text="Response", relief=tk.RIDGE)
        self.stat_frame.grid(row=3, column=0, columnspan = 4,sticky="ews", padx=(0,5), ipadx=5)
        self.stat_frame.rowconfigure(1, weight=1)
        self.stat_frame.columnconfigure(1, weight=1)
        self.response = st.ScrolledText(self.stat_frame, 
                            width = 80,  
                            height = 8,  
                            font = ("Times New Roman", 12)) 
        self.response.grid(row=0, column=1, sticky=tk.W, padx=(10,10))
        self.response.insert(tk.INSERT, "waiting for response")
    # - - Quit button in the lower right corner - - - - - - - - - - - - - - - - - - - - - - -
        self.quit_button = ttk.Button(self.root, text="Quit", command=self.root.destroy)
        self.quit_button.grid(row=4, column=3, sticky=tk.E)

# Create the entire GUI app
app = AI_Main()

# Start the GUI event loop
app.root.mainloop()