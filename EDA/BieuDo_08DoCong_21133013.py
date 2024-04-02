import customtkinter
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import pandas as pd
import seaborn as sns

class ThongSoWindow(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.grid_rowconfigure(10, weight=10)
        
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Chon Nguong Nhỏ")
        self.entry.grid(row=1, column=0)
        self.button = customtkinter.CTkButton(self, text="ReloadMin",command=self.ReloadNguong)
        self.button.grid(row=2, column=0)
               
        self.entry2 = customtkinter.CTkEntry(self, placeholder_text="Chon Nguong Lớn")
        self.entry2.grid(row=3, column=0)
        self.button2 = customtkinter.CTkButton(self, text="ReloadMax",command=self.ReloadNguong)
        self.button2.grid(row=4, column=0)
    def ReloadNguong(self):
        self.valuemin= float(self.entry.get())
        self.valuemax= float(self.entry2.get())
        print(self.valuemin)
        print(self.valuemax)
        self.master.ReloadNguong(self.valuemin,self.valuemax)
        
        
class BieuDoWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.geometry("1200x600")
        self.title("Đồ Án.")
        self.maxsize(1200, 600)
        self.minsize(1200, 600)
    def display(self):
        self.valuemax=10
        self.valuemin=0
        self.optionmenu_var_z = tk.StringVar()
        self.optionmenu = customtkinter.CTkOptionMenu(self, values=["Plot Graph", "Bar Graph", "Line Graph","Scatter Graph","Hist","Kdeplot"],
                                         command=self.optionmenu_bieudo, variable=self.optionmenu_var_z)
        self.optionmenu.set("Plot Graph")
        self.optionmenu.pack(side = tk.TOP)
        self.list_entry=ThongSoWindow(self)
        self.list_entry.pack(side = tk.LEFT)
        '''self.entry = customtkinter.CTkEntry(self, placeholder_text="Chon Nguong")
        self.entry.pack(side = tk.LEFT)
        self.button = customtkinter.CTkButton(self, text="Reload",command=self.ReloadNguong)
        self.button.pack(side = tk.LEFT,pady=50,ipady=50)'''
    def HienThiNoiDung(self):
        try:
            #self.textbox = ...
            z,dl = self.data.ZCORES(self.valuemin,self.valuemax)
            self.listbox.InsertDataGridView(list(dl.columns),dl)
            self.textbox.delete(0,tk.END)
            self.textbox.insert(0,f"{dl.shape}")
        except:
            pass
    def ReloadNguong(self,min,max):
        self.valuemin=min
        self.valuemax=max
        self.optionmenu_bieudo(self.optionmenu_var_z.get())
    def insertdata(self,data,listbox,textbox):
        self.data = data
        self.listbox = listbox
        self.textbox = textbox
        #print("ThanhCong")
        #print(self.data.GiaTriChuanHoa4())
    def optionmenu_bieudo(self,choice):
        z_core=self.data.ZCORES_matran(self.valuemin,self.valuemax)
        if (choice=="Plot Graph"):
            self.plot(z_core)
        elif (choice=="Bar Graph"):
            self.bar_line(z_core,"","","",'bar')
        elif (choice=="Line Graph"):
            self.bar_line(z_core,'','','','line')
        elif (choice=="Hist"):
            self.bar_line(z_core,'','','','hist')
        elif (choice=="Kdeplot"):
            self.kdeplot(z_core,"Number","Value")
        else :#"Scatter Graph"
            try:
                self.canvs_clear()
                print("Thanh cong")
            except:
                pass
            self.scatter(z_core,'','','')    
    def plot(self,y): 
        try:
            self.canvs_clear()
            print("Thanh cong")
        except:
            pass 
        # the figure that will contain the plot
        fig = Figure(figsize = (5, 5),dpi = 100)
        # adding the subplot
        plot1 = fig.add_subplot(111)
        # plotting the graph
        curve,=plot1.plot(y)
        # creating the Tkinter canvas
        # containing the Matplotlib figure
        self.canvas = FigureCanvasTkAgg(fig, master = self)  
        self.canvas.draw()
        # placing the canvas on the Tkinter window
        self.canvas.get_tk_widget().pack()
        # creating the Matplotlib toolbar
        self.toolbar = NavigationToolbar2Tk(self.canvas,self)
        self.toolbar.update()
        # placing the toolbar on the Tkinter window
        self.canvas.get_tk_widget().pack()
        
        xdata = curve.get_xdata()
        ydata = curve.get_ydata()
        print(f"{xdata} {ydata}")
    def bar_line(self,df1,x_name,y_name,title,loaibd): 
        try:
            self.canvs_clear()
            print("Thanh cong")
        except:
            pass 
        figure1 = plt.Figure(figsize=(6, 5), dpi=100)
        ax1 = figure1.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(figure1, self)
        self.canvas.get_tk_widget().pack()
        #df1 = df1[[x_name, y_name]].groupby(x_name).sum()
        df1.plot(kind=loaibd, legend=True, ax=ax1)
        ax1.set_title(title)
        self.toolbar = NavigationToolbar2Tk(self.canvas,self)
        self.toolbar.update()
        # placing the toolbar on the Tkinter window
        self.canvas.get_tk_widget().pack()
    def scatter(self,df3,x_name,y_name,title):
        figure3 = plt.Figure(figsize=(5, 4), dpi=100)
        ax3 = figure3.add_subplot(111)
        ax3.scatter(df3[x_name], df3[y_name], color='g')
        self.canvas = FigureCanvasTkAgg(figure3, self)
        self.canvas.get_tk_widget().pack()
        ax3.legend([y_name])
        ax3.set_xlabel(x_name)
        ax3.set_title(title)
        # creating the Matplotlib toolbar
        self.toolbar = NavigationToolbar2Tk(self.canvas,self)
        self.toolbar.update()
        # placing the toolbar on the Tkinter window
        self.canvas.get_tk_widget().pack()
            
    def canvs_clear(self):#Clear canvas
        self.canvas.get_tk_widget().pack_forget()     
        self.toolbar.pack_forget()  
    def kdeplot(self,data: pd.DataFrame,xlabel,ylabel):
        try:
            self.canvs_clear()
        except:
            pass
        figure3 = plt.Figure(figsize=(5, 4), dpi=100)
        ax3 = figure3.add_subplot(111)
        
        self.canvas = FigureCanvasTkAgg(figure3, self)
        self.canvas.get_tk_widget().pack()
        sns.kdeplot(data=data, color='b', fill=True,ax=ax3)
        ax3.set_xlabel(xlabel)
        ax3.set_ylabel(ylabel)
        self.toolbar = NavigationToolbar2Tk(self.canvas,self)
        self.toolbar.update()
        self.canvas.get_tk_widget().pack()   
if __name__=="__main__":
    pass