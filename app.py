import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from tkinter import scrolledtext
import pandas as pd
import io

class App:
    encoding = ('utf-8','iso-8859-1','windows-1252','iso-8859-2','utf-16le','utf-16be','ascii','cp1252')
    def __init__(self,icon_path:str,title = "App",width:int = 720,height:int = 400,**karg):
        """the main window for the app with 
        all the argument needed for the app"""
        self.root = tk.Tk()
        self.root.title(title)
        icon_image = tk.PhotoImage(file=icon_path)
        self.root.iconphoto(True,icon_image)
        self.root.geometry(f"{width}x{height}")
        self.root.resizable(False, False)
        self.root.columnconfigure((0,1,2),weight=1,uniform='a')
        self.root.rowconfigure((0,1),weight=1,uniform='a')
        self.root.rowconfigure(2,weight=8,uniform='a')
    
    def path_selection(self):
        """open broseing window to choose the path"""
        path = filedialog.askopenfilename()
        self.path.set(path)

    def choose_data_w(self):
        """create butten and label for open browsing window by calling 
        (path_selection) function to select the path of the data"""
        self.path = tk.StringVar(value='Data path...')
        Button = tk.Button(self.root,text="choose file...",command=self.path_selection)
        Label = tk.Label(self.root,relief='ridge',textvariable=self.path)
        Button.grid(row=0,column=0)
        Label.grid(row=0,column=1,columnspan=2,sticky="w")

    def coding_list_w(self):
        """Combo list for choosing the the encoding code for the data"""
        codes = App.encoding
        self.selected_code = tk.StringVar(value=codes[0])
        label = tk.Label(self.root,text="Enter a encoding")
        label.grid(row=1,column=0)
        box_codes = ttk.Combobox(self.root, textvariable=self.selected_code, values=codes,state='readonly')
        box_codes.grid(row=1,column=1,sticky="w")
        ok = tk.Button(self.root,text="OK",command=self.load_data)
        ok.grid(row=1,column=2,sticky="we",padx=50)

    def load_data(self):
        """Loading the data to (df) var
        and display info by calling (info_w) function"""
        self.df = pd.read_csv(self.path.get(),encoding=self.selected_code.get())
        self.display_info(self.df)
        pro_button = tk.Button(self.root,text="Preprossing",command=self.load_window)
        pro_button.grid(row=2,column=2,ipadx=35,ipady=10,pady=15,sticky="n")
        vis_button = tk.Button(self.root,text="Visualzation",command=self.load_window)
        vis_button.grid(row=2,column=2,ipadx=35,ipady=10)
        model_button = tk.Button(self.root,text="Train the model",command=self.load_window)
        model_button.grid(row=2,column=2,ipadx=35,ipady=10,pady=15,sticky="s")
    
    def display_info(self,df):
        buffer = io.StringIO()
        df.info(buf=buffer)
        info = tk.StringVar(value=buffer.getvalue())
        label = scrolledtext.ScrolledText(self.root,width=40,height=15,relief='ridge')
        label.insert(tk.END,info.get())
        label.grid(row=2,column=0,columnspan=2,padx=10,pady=10,sticky="nesw")

    def load_window(self):
        print("lol")
        
    def run(self):
        """Run the main loop."""
        self.choose_data_w()
        self.coding_list_w()
        self.root.mainloop()
