import tkinter as tk
import customtkinter
from tkinter import ttk
import pandas as pd


class Datagrid(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        #Configure.
        self.Style = ttk.Style()
        self.Style.theme_use("clam")
        self.Style.configure('Treeview',\
                    background="white",
                    foreground="black",
                    rowheight=25,
                    fieldbackground="white"
                    
            )
        self.Style.configure("Treeview.Heading",\
                    background="black", foreground="white")
        self.Style.map('Treeview',background=[('selected','#7fedf7')])
        #self.ThucHien(3,["ID","Company","Company2"])
    def SoLuongCot(self,n):
        sl_cot=[]
        for i in range(1,n+1):
            sl_cot.append(f"c{i}")
        return sl_cot
    def clear_all(self):
       for item in self.tree.get_children():
            self.tree.delete(item)
    def ThucHien(self,sl_cot,label_cot:list,dulieu:pd.DataFrame):#,dulieu:pd.DataFrame
        try:
            self.clear_all()
        except:
            pass
        self.game_scroll_y = ttk.Scrollbar(self.master)
        self.game_scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        self.game_scroll_x = ttk.Scrollbar(self.master,orient='horizontal')
        self.game_scroll_x.pack(side= tk.BOTTOM,fill=tk.X)
        columns = self.SoLuongCot(sl_cot)    
        self.tree = ttk.Treeview(self.master, column=(columns), show='headings', height=8,\
                                    yscrollcommand=self.game_scroll_y.set, xscrollcommand =self.game_scroll_x.set)
        self.game_scroll_y.config(command=self.tree.yview)
        self.game_scroll_x.config(command=self.tree.xview)
        #Them vao so luong cot
        for i in range(0,sl_cot):
            self.tree.column(f"# {i+1}",anchor=customtkinter.CENTER)
            self.tree.heading(f"# {i+1}", text=label_cot[i])        
        #Chen du lieu
        dem=0
        for i in dulieu.values.tolist():
            dem+=1
            self.tree.insert('', 'end', text=f"{dem}", values=(i))
        self.tree.pack(expand=True, fill="both")

if __name__ == "__main__":
    customtkinter.set_appearance_mode("dark")
    root = customtkinter.CTk()
    datagrid = Datagrid(root)
    root.mainloop()