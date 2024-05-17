import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from tkinter import scrolledtext
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
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
        self.data_name = path.split("/")[-1].split(".")[0]

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
        ok = tk.Button(self.root,text="Load",command=self.load_data)
        ok.grid(row=1,column=2,sticky="we",padx=50)

    def load_data(self):
        """Loading the data to (df) var
        and display info by calling (info_w) function"""
        self.df = pd.read_csv(self.path.get(),encoding=self.selected_code.get())
        self.display_info(self.df)
        pro_button = tk.Button(self.root,text="Preprossing",command=lambda :self.load_window("pre"))
        pro_button.grid(row=2,column=2,ipadx=35,ipady=10,pady=15,sticky="n")
        vis_button = tk.Button(self.root,text="Visualzation",command=lambda :self.load_window("vis"))
        vis_button.grid(row=2,column=2,ipadx=35,ipady=10)
        model_button = tk.Button(self.root,text="Train the model",command=lambda :self.load_window("train"))
        model_button.grid(row=2,column=2,ipadx=35,ipady=10,pady=15,sticky="s")
    
    def display_info(self,df):
        buffer = io.StringIO()
        df.info(buf=buffer)
        info = tk.StringVar(value=buffer.getvalue())
        label = scrolledtext.ScrolledText(self.root,width=40,height=15,relief='ridge')
        label.insert(tk.END,info.get())
        label.grid(row=2,column=0,columnspan=2,padx=10,pady=10,sticky="nesw")

    def load_window(self,choose):
        if (choose =="pre"):
            self.pre_windowp = pre_window(perent_window=gui,icon_path="./assets/AI-icon.png")
            self.pre_windowp.load_GUI()
        elif (choose == "vis"):
            self.vis_windowp = vis_window(perent_window=gui,icon_path="./assets/AI-icon.png")
            self.vis_windowp.load_GUI()
        elif (choose == "train"):
            self.ml_windowp = ML_window(perent_window=gui,icon_path="./assets/AI-icon.png")
            self.ml_windowp.load_GUI()
        
    def run(self):
        """Run the main loop."""
        self.choose_data_w()
        self.coding_list_w()
        self.root.mainloop()

class pre_window:
    def __init__(self,perent_window,icon_path:str,title = "Preprossing",width:int = 720,height:int = 400,**karg):
        """the main window for the app with 
        all the argument needed for the app"""
        self.perant = perent_window
        self.pre_window = tk.Toplevel()
        
        self.data_name = self.perant.data_name
        self.pre_window.title(title)
        icon_image = tk.PhotoImage(file=icon_path)
        self.pre_window.iconphoto(True,icon_image)
        self.pre_window.geometry(f"{width}x{height}")
        self.pre_window.resizable(False, False)
        self.pre_window.columnconfigure((0,1,2),weight=1,uniform='a')
        self.pre_window.rowconfigure((0,1,2,3,4,5,6),weight=1,uniform='a')

    def load_GUI(self):
        """Load the labels and buttens in preprossing window"""

        # drop columns
        label_dc = tk.Label(self.pre_window,relief='ridge',text="Drop Column :")
        label_dc.grid(row=0,column=0,padx=10,sticky="we")
        columns = [col for col in self.perant.df.columns]
        dc_columns=columns.copy()
        dc_columns.insert(0,"No Drop")
        self.drop_col = tk.StringVar(value="No Drop")
        combobox_dc = ttk.Combobox(self.pre_window,textvariable=self.drop_col,values=dc_columns,state='readonly')
        combobox_dc.grid(row=0,column=1,columnspan=2,padx=10,sticky="we")
        # drop duplicates
        label_dd = tk.Label(self.pre_window,relief='ridge',text="Drop Duplcats :")
        label_dd.grid(row=1,column=0,padx=10,sticky="we")
        self.var_dd = tk.StringVar(value="No")
        redio_n_dd = ttk.Radiobutton(self.pre_window,text="No",variable=self.var_dd,value="No")
        redio_y_dd = ttk.Radiobutton(self.pre_window,text="Yes",variable=self.var_dd,value="Yes")
        redio_y_dd.grid(row=1,column=1)
        redio_n_dd.grid(row=1,column=2)
        # drop nulls
        label_dn = tk.Label(self.pre_window,relief='ridge',text="Drop Nulls :")
        label_dn.grid(row=2,column=0,padx=10,sticky="we")
        columns_dn = columns.copy()
        columns_dn.insert(0,"No Drop")
        columns_dn.insert(1,"All columns")
        self.radio_var_dn = tk.StringVar(value="any")
        self.combo_dn = tk.StringVar(value="No Drop")
        redio_all_dn = ttk.Radiobutton(self.pre_window,text="All",variable=self.radio_var_dn,value="all")
        redio_any_dn = ttk.Radiobutton(self.pre_window,text="Any",variable=self.radio_var_dn,value="any")
        combobox_dn = ttk.Combobox(self.pre_window,textvariable=self.combo_dn,values=columns_dn,state='readonly')
        redio_any_dn.grid(row=2,column=1,sticky="w",padx=50)
        redio_all_dn.grid(row=2,column=1,sticky="e",padx=50)
        combobox_dn.grid(row=2,column=2,padx=10,sticky="we")

        # scale
        label_scale = tk.Label(self.pre_window,relief='ridge',text="Scale Column :")
        label_scale.grid(row=3,column=0,padx=10,sticky="we")
        self.scale_technique = tk.StringVar(value="MinMaxScaler")
        self.scale_column1 = tk.StringVar(value="No Scale")
        self.scale_column2 = tk.StringVar(value="No Scale")
        technique = ["MinMaxScaler","StandardScaler","Normalizer"]
        columns_scale = columns.copy()
        columns_scale.insert(0,"No Scale")
        combobox_scalet = ttk.Combobox(self.pre_window,textvariable=self.scale_technique,values=technique,state='readonly')
        combobox_scalec1 = ttk.Combobox(self.pre_window,textvariable=self.scale_column1,width=10,values=columns_scale.copy(),state='readonly')
        combobox_scalec2 = ttk.Combobox(self.pre_window,textvariable=self.scale_column2,width=10,values=columns_scale.copy(),state='readonly')
        combobox_scalet.grid(row=3,column=1,padx=10,sticky="we")
        combobox_scalec1.grid(row=3,column=2,padx=10,sticky="w")
        combobox_scalec2.grid(row=3,column=2,padx=10,sticky="e")
        
        #Encoder
        label_enco = tk.Label(self.pre_window,relief='ridge',text="Encode Column :")
        label_enco.grid(row=4,column=0,padx=10,sticky="we")
        self.enco_technique = tk.StringVar(value="One Hot Encoder")
        self.enco_column = tk.StringVar(value="No Encoding")
        encoders = ["One Hot Encoder","Label Encoder"]
        columns_enco = columns.copy()
        columns_enco.insert(0,"No Encoding")
        combobox_encot = ttk.Combobox(self.pre_window,textvariable=self.enco_technique,values=encoders,state='readonly')
        combobox_encoc = ttk.Combobox(self.pre_window,textvariable=self.enco_column,values=columns_enco,state='readonly')
        combobox_encot.grid(row=4,column=1,padx=10,sticky="we")
        combobox_encoc.grid(row=4,column=2,padx=10,sticky="we")

        # apply and save buttons
        button_apply = tk.Button(self.pre_window,text="Apply",command=self.apply)
        button_apply.grid(row=6,column=0,padx=10,pady=10,sticky="we")
        button_apply = tk.Button(self.pre_window,text="Save",command=self.save)
        button_apply.grid(row=6,column=2,padx=10,pady=10,sticky="we")

    def apply(self):
        # drop columns
        if self.drop_col.get() != "No Drop":
            self.perant.df = self.perant.df.drop(self.drop_col.get(),axis="columns")
        # drop duplicates
        if self.var_dd.get() != "No":
            self.perant.df.drop_duplicates()
        # drop nulls
        if self.combo_dn.get() != "No Drop":
            if self.combo_dn.get() == "All columns":
                self.perant.df = self.perant.df.dropna(how=self.radio_var_dn.get())
            else:
                self.perant.df[self.combo_dn.get()] = self.perant.df[self.combo_dn.get()].dropna(how=self.radio_var_dn.get())
        # scale
        if (self.scale_column1.get()!="No Scale") and (self.scale_column2.get()!="No Scale"):
            if self.scale_technique.get()=="StandardScaler":
                scaler = StandardScaler()
                scaled = scaler.fit_transform(self.perant.df[[self.scale_column1.get(),self.scale_column2.get()]])
                self.perant.df[self.scale_column1.get()] = scaled[:,0]
                self.perant.df[self.scale_column2.get()] = scaled[:,1]
                
            elif self.scale_technique.get()=="MinMaxScaler":
                scaler = MinMaxScaler()
                scaled = scaler.fit_transform(self.perant.df[[self.scale_column1.get(),self.scale_column2.get()]])
                self.perant.df[self.scale_column1.get()] = scaled[:,0]
                self.perant.df[self.scale_column2.get()] = scaled[:,1]
                
            elif self.scale_technique.get()=="Normalizer":
                scaler = Normalizer()
                scaled = scaler.fit_transform(self.perant.df[[self.scale_column1.get(),self.scale_column2.get()]])
                self.perant.df[self.scale_column1.get()] = scaled[:,0]
                self.perant.df[self.scale_column2.get()] = scaled[:,1]
                
            
        if self.enco_column.get()!="No Encoding":
            if self.enco_technique.get()=="One Hot Encoder":
                onehot=pd.get_dummies(self.perant.df[self.enco_column.get()])
                self.perant.df=self.perant.df.drop([self.enco_column.get()],axis="columns")
                self.perant.df = self.perant.df.join(onehot)
            elif self.enco_technique.get()=="Label Encoder":
                labelcode = LabelEncoder()
                self.perant.df[self.enco_column.get()] = labelcode.fit_transform(self.perant.df[self.enco_column.get()])

        self.load_GUI()
    
    def save(self):
        self.perant.df.to_csv(f"data/pre_{self.data_name}.csv",index=False)
        self.load_GUI()


class vis_window():
    def __init__(self,perent_window,icon_path:str,title = "Visualization",width:int = 720,height:int = 400,**karg):
        """the main window for the app with 
        all the argument needed for the app"""
        self.perant = perent_window
        self.df_vis = self.perant.df
        self.vis_window = tk.Toplevel()
        self.vis_window.title(title)
        icon_image = tk.PhotoImage(file=icon_path)
        self.vis_window.iconphoto(True,icon_image)
        self.vis_window.geometry(f"{width}x{height}")
        self.vis_window.resizable(False, False)
        self.vis_window.columnconfigure(0,weight=4,uniform='a')
        self.vis_window.columnconfigure(1,weight=1,uniform='a')
        self.vis_window.rowconfigure((0,1,2,3),weight=1,uniform='a')

    def load_GUI(self):
        columns = [col for col in self.df_vis.columns]
        self.type = tk.StringVar(value="Line Plot")
        self.col1 = tk.StringVar(value=columns[0])
        self.col2 = tk.StringVar(value=columns[1])
        self.plots = ["Line Plot","Bar Plot","Scatter Plot"]
        label_type = tk.Label(self.vis_window,relief='ridge',text="Plot Type")
        label_col1 = tk.Label(self.vis_window,relief='ridge',text="column_x")
        label_col2 = tk.Label(self.vis_window,relief='ridge',text="column_y")
        combobox_type = ttk.Combobox(self.vis_window,textvariable=self.type,values=self.plots,state='readonly')
        combobox_col1 = ttk.Combobox(self.vis_window,textvariable=self.col1,width=10,values=columns.copy(),state='readonly')
        combobox_col2 = ttk.Combobox(self.vis_window,textvariable=self.col2,width=10,values=columns.copy(),state='readonly')
        label_type.grid(row=0,column=1,padx=10,pady=25,sticky="nwe")
        label_col1.grid(row=1,column=1,padx=10,pady=25,sticky="nwe")
        label_col2.grid(row=2,column=1,padx=10,pady=25,sticky="nwe")
        combobox_type.grid(row=0,column=1,padx=10,pady=20,sticky="swe")
        combobox_col1.grid(row=1,column=1,padx=10,pady=20,sticky="swe")
        combobox_col2.grid(row=2,column=1,padx=10,pady=20,sticky="swe")
        
        #Plot
        button_plot = tk.Button(self.vis_window,text="Plot",command=self.polt)
        button_plot.grid(row=3,column=1,padx=10,pady=10,sticky="nwe")
        button_save = tk.Button(self.vis_window,text="Save",command=self.save)
        button_save.grid(row=3,column=1,padx=10,pady=10,sticky="swe")

    def polt(self):
        self.fig , self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig,master=self.vis_window)
        self.widget = self.canvas.get_tk_widget()
        self.widget.grid(row=0,column=0,rowspan=4,padx=10,pady=10)
        if self.type.get() == self.plots[0]:
            self.ax.plot(self.df_vis[self.col1.get()],self.df_vis[self.col2.get()])
        elif self.type.get() == self.plots[1]:
            self.ax.Bar(self.df_vis[self.col1.get()],self.df_vis[self.col2.get()])
        elif self.type.get() == self.plots[2]:
            self.ax.scatter(self.df_vis[self.col1.get()],self.df_vis[self.col2.get()])

    def save(self):
        self.fig.savefig(f"Figs/{self.col1.get()} VS {self.col2.get()}.png")



class ML_window:
    def __init__(self,perent_window,icon_path:str,title = "ML",width:int = 720,height:int = 400,**karg):
        """the main window for the app with 
        all the argument needed for the app"""
        self.perant = perent_window
        self.ml_window = tk.Toplevel()
        self.ml_window.title(title)
        icon_image = tk.PhotoImage(file=icon_path)
        self.ml_window.iconphoto(True,icon_image)
        self.ml_window.geometry(f"{width}x{height}")
        self.ml_window.resizable(False, False)
        self.ml_window.columnconfigure((0,1,2),weight=1,uniform='a')
        self.ml_window.rowconfigure((0,1,2,3,4,5,6),weight=1,uniform='a')

    def load_GUI(self):
        pass





gui = App(icon_path="./assets/AI-icon.png",title="ML-GUI")