import customtkinter
import tkinter as tk
import pandas as pd


#CTkToplevel  CTk
#Lua chon thuoc tinh de chuan hoa cac gia tri chuoi.
class EDAWindowCH(customtkinter.CTkToplevel):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def DuLieuAttribute(self,dl):
        self.dl = dl #Truyen lop vao
    def display(self):
        self.geometry("1000x500")
        self.title("Lựa chọn thuộc tính mục tiêu")
        self.grid_rowconfigure(9)  # configure grid system
        self.grid_columnconfigure(5)
        self.maxsize(1000, 500)
        self.minsize(1000, 500)
        #Tao ngan vach nhan tao
        self.nganvachngang = customtkinter.CTkLabel(self, text = "",fg_color="transparent")
        #Tao vanh ngan doc nhan tao
        self.nganvachdoc = customtkinter.CTkLabel(self, text = "",fg_color="transparent",width=120)
        
        
        self.nganvachdoc.grid(row=0,column=0,sticky="nsew")
        #Cac button xu ly
        #Thiết lập label
        self.name_label=customtkinter.CTkLabel(self, text = "Các Thuộc tính",fg_color="transparent",text_color="green",font=('Roboto',16))
        self.name_label.grid(row=0,column=1,sticky="nsew")
        self.name_label=customtkinter.CTkLabel(self, text = "Các Thuộc Tính Trích Lọc",fg_color="transparent",text_color="green",font=('Roboto',16))
        self.name_label.grid(row=0,column=4,sticky="nsew")
        #2 TextBox
        self.textbox_nguon = tk.Listbox(self,width=50,height=20)
        self.textbox_nguon.grid(row=1, column=1,rowspan=5, sticky="nsew")
        #Vach ngan
        self.nganvachdoc1 = customtkinter.CTkLabel(self, text = "",fg_color="transparent",width=120)
        self.nganvachdoc1.grid(row=1,column=3,sticky="nsew")
        
        self.textbox_dich = tk.Listbox(self,width=50)
        self.textbox_dich.bind("<Button-3>", self.ButtonRight)
        self.textbox_dich.grid(row=1, column=4,rowspan=5, sticky="nsew")
        self.nganvachngang.grid(row=6, column=1,columnspan=5)
        #Nut Chuan Hoa
        
        self.bchuanhoa = customtkinter.CTkEntry(self, placeholder_text="k=")
        self.bchuanhoa.grid(row=7,column=1)
        
        
        self.bchuanhoa2 = customtkinter.CTkButton(self, text="Trích Lọc",width=150,border_width=5,border_color='#2c0568',font=('Roboto',16),command=self.TrichLoc)
        self.bchuanhoa2.grid(row=7,column=3)
        #Vach ngan
        self.nganvachngang1 = customtkinter.CTkLabel(self, text = "",fg_color="transparent")
        self.nganvachngang1.grid(row=8, column=1,columnspan=5)
        #Tu dong dua vao cac thuoc tinh da chon.
        self.values = list(self.dl.GiaTriChuanHoa7().columns)
        self.optionmenu_var = tk.StringVar()
        self.optionmenu = customtkinter.CTkOptionMenu(self, values=self.values,font=('Roboto',16),
                                         command=self.optionmenu_thuoctinh,variable=self.optionmenu_var)
        self.optionmenu.set(self.values[0])
        self.optionmenu.grid(row=9,column=1) 
    def CacThuocTinh(self):  
        self.textbox_nguon.delete(0,tk.END) 
        for i in self.values:
            self.textbox_nguon.insert(tk.END,i)
    def optionmenu_thuoctinh(self,choice):
        pass
        #self.choice = choice #Xu lu mlap
        #self.textbox_nguon.delete(0,tk.END)
        #for i in list(self.dl.GiaTriChuanHoa2()[choice].drop_duplicates()):
        #    self.textbox_nguon.insert(tk.END,i)
        #print(self.df)
        
        
    def ChuanHoa(self):
        pass
    
    
    def ButtonRight(self,e):
         if self.textbox_nguon.size() > 0 :
            Cong08_21133013 = tk.Menu(self.textbox_nguon, tearoff = tk.FALSE)
            Cong08_21133013.add_command(label = "Remove",command=self.RemoveRight)
            Cong08_21133013.tk_popup(e.x_root, e.y_root)
    def RemoveRight(self):
        i = 0
        CongDo08_013 = self.textbox_dich.curselection() # lấy ds các vị trí chọn
        for i in reversed(CongDo08_013):
            self.textbox_dich.delete(i)
    
    def TrichLoc(self):
        self.attribute = self.dl.EDA(self.optionmenu_var.get(),int(self.bchuanhoa.get()))
        self.textbox_dich.delete(0,tk.END)
        for i in self.attribute:
            self.textbox_dich.insert(tk.END,i)

if __name__=="__main__":
    App = EDAWindowCH()
    App.DuLieuAttribute([],[])
    App.display()
    App.mainloop()