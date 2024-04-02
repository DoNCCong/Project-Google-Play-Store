import numpy as np
import pandas as dp
from DataGrid_08DoCong_21133013 import *
from PIL import Image
from tkinter import filedialog
from TroLy_08DoCong_21133013 import *
from XuLyDuLieu_08DoCong_21133013 import *

from BieuDo_08DoCong_21133013 import *
from EDA_08DoCong_21133013 import *
# Tạo thêm một level window để lựa chọn đồ thị và giá trị.

#####
#Lop Hien Thi Cua So Rieng.
class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")

        self.label = customtkinter.CTkLabel(self, text="ToplevelWindow")
        self.label.pack(padx=20, pady=20)
#Tao khung frame danh cho text
class FrameText(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.ldulieutho=customtkinter.CTkLabel(self,text="",text_color='green' ,fg_color= "transparent",corner_radius=10)
        self.ldulieutho.grid(row=0,column=0)
        self.my_text= customtkinter.CTkTextbox(self,width=800, corner_radius=0,scrollbar_button_hover_color='dark_color')
        self.my_text.grid(sticky="nsew")
        #self.my_text.insert("0.0", "This is a text!\n" * 20)

#Lua chon thuoc tinh de chuan hoa cac gia tri chuoi.
class AttributeWindowCH(customtkinter.CTkToplevel):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def DuLieuAttribute(self,data,ucbang,dl):
        self.df = data
        self.UCbang = ucbang#Chen bang vao
        self.dl = dl #Truyen lop vao
    def display(self):
        self.geometry("1000x500")
        self.title("Lựa chọn thuộc tính cần chuan hoa")
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
        self.name_label=customtkinter.CTkLabel(self, text = "Các Giá Trị Trong 1 Thuộc tính",fg_color="transparent",text_color="green",font=('Roboto',16))
        self.name_label.grid(row=0,column=1,sticky="nsew")
        self.name_label=customtkinter.CTkLabel(self, text = "Các Thuộc Tính Cần Chuẩn Hóa",fg_color="transparent",text_color="green",font=('Roboto',16))
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
        self.bchuanhoa = customtkinter.CTkButton(self, text="Chuẩn Hóa",width=150,border_width=5,border_color='#2c0568',font=('Roboto',16)\
                                                ,command=self.ChuanHoa)
        self.bchuanhoa.grid(row=7,column=1)
        self.bchuanhoa2 = customtkinter.CTkButton(self, text="Làm Sạch",width=150,border_width=5,border_color='#2c0568',font=('Roboto',16),command=self.VeBang)
        self.bchuanhoa2.grid(row=7,column=3)
        #Vach ngan
        self.nganvachngang1 = customtkinter.CTkLabel(self, text = "",fg_color="transparent")
        self.nganvachngang1.grid(row=8, column=1,columnspan=5)
        #Tu dong dua vao cac thuoc tinh da chon.
        values = list(self.df.columns)
        self.optionmenu_var = tk.StringVar()
        self.optionmenu = customtkinter.CTkOptionMenu(self, values=values,font=('Roboto',16),
                                         command=self.optionmenu_thuoctinh,variable=self.optionmenu_var)
        self.optionmenu.set(values[0])
        self.optionmenu.grid(row=9,column=1)    
    def optionmenu_thuoctinh(self,choice):
        self.choice = choice #Xu lu mlap
        self.textbox_nguon.delete(0,tk.END)
        for i in list(self.dl.GiaTriChuanHoa2()[choice].drop_duplicates()):
            self.textbox_nguon.insert(tk.END,i)
        #print(self.df)
    def ChuanHoa(self):
        if( not (self.choice in list(self.textbox_dich.get(0,self.textbox_dich.size())))):
            self.textbox_dich.insert(tk.END,self.choice)
    
    
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
    
    def VeBang(self):
        for i in list(self.textbox_dich.get(0,tk.END)):
            print(self.dl.ChuanHoaSo(i))
        self.df = self.dl.GiaTriChuanHoa3()
        #print(self.df)
        self.UCbang.InsertDataGridView(list(self.df.columns),self.df)
        #self.textbox.delete(0,tk.END)
        #self.textbox.insert(0,f"{self.df.shape}")
#Lua chon thuoc tinh window.
class AttributeWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("1000x500")
        self.title("Lựa chọn thuộc tính cần loại bỏ")
        self.grid_rowconfigure(7)  # configure grid system
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
        #self.entry = customtkinter.CTkEntry(self, placeholder_text="ThuocTinh",width=100)
        #self.entry.grid(row=0,column=1,sticky="nsew")
        #Thiết lập textbox (khi apply = dùng for nạp các thuộc tính vào thay vì nhập từ textbox )
        #DoCong08_2 = tk.Entry(DoCong08, width = 30) # Entry = cho nhập DL vào
        #DoCong08_2.place(x = 120, y = 15)
        
        #Khoi tao cac button
        self.button1 = customtkinter.CTkButton(self, text="Move Right",width=150,border_width=5,border_color='#2c0568',command=self.Move_To_Left)
        self.button1.grid(row=1,column=2)
        self.button2 = customtkinter.CTkButton(self, text="Move Left",width=150,border_width=5,border_color='#2c0568',command=self.Move_To_Right)
        self.button2.grid(row=2,column=2)
        self.button3 = customtkinter.CTkButton(self, text="Move All Right",width=150,border_width=5,border_color='#2c0568',command=self.Move_All_Right)
        self.button3.grid(row=3,column=2)
        self.button4 = customtkinter.CTkButton(self, text="Move All Left",width=150,border_width=5,border_color='#2c0568',command = self.Move_All_Left)
        self.button4.grid(row=4,column=2)
        self.button5 = customtkinter.CTkButton(self, text="Remove",width=150,border_width=5,border_color='#2c0568',command=self.RemoveListBox)
        self.button5.grid(row=5,column=2)
        #2 TextBox
        #self.textbox_nguon = customtkinter.CTkTextbox(master=self, width=400,height=400, corner_radius=0,scrollbar_button_color="black",font=('Roboto',16))
        self.textbox_nguon = tk.Listbox(self,width=50,height=20)
        self.textbox_nguon.bind("<Button-3>", self.ButtonLeft)
        self.textbox_nguon.grid(row=1, column=1,rowspan=5, sticky="nsew")
        
        #self.textbox_nguon.insert("0.0", "Some example text!\n" * 50)
        #self.textbox_dich = customtkinter.CTkTextbox(master=self, width=400, corner_radius=0,scrollbar_button_color="black",font=('Roboto',16))
        self.textbox_dich = tk.Listbox(self,width=50)
        self.textbox_dich.grid(row=1, column=4,rowspan=5, sticky="nsew")
        self.textbox_dich.bind("<Button-3>", self.ButtonRight)
        #self.textbox_dich.insert("0.0", "Some example text!\n" * 50)
        
        
        #Tao ngan vach nhan tao
        #self.nganvachngang = customtkinter.CTkLabel(self, text = "",fg_color="transparent")
        self.nganvachngang.grid(row=6, column=1,columnspan=5)
        #Check box de tu loai bo cac thuoc tinh co qua nhieu o rong
        self.check_var = tk.StringVar()
        self.checkbox = customtkinter.CTkCheckBox(self, text="Tự động xử lý các thuộc tính có nhiều ô null",font=('Roboto',16),
                                     variable=self.check_var, onvalue="on", offvalue="off",command=self.XuLyNull)
        self.checkbox.grid(row=7, column=1,columnspan=5)
        
        #Thuc hien mot button de thuc thi
        self.button_table = customtkinter.CTkButton(self, text="Thực thi",command=self.VeBang)
        self.button_table.grid(row=9,column=2)
    
    
    def VeBang(self):
        self.thongtinchuan = self.df.LoaiBoThuocTinh(self.TakeValueListBoxRight())
        #print(self.thongtinchuan)
        self.listbox2.InsertDataGridView(list(self.thongtinchuan.columns),self.thongtinchuan)
        self.entry_of_frame_text_two.delete(0,tk.END)
        self.entry_of_frame_text_two.insert(0,f"{self.thongtinchuan.shape}")
    #Su dung cho ham check var
    def XuLyNull(self):
        if(self.check_var.get()=="on"):
            #Dua cac cot co gia tri null sang ben kia
            list_str = list(self.df.CotCoGiaTriRong())
            for i in list_str:
                self.textbox_dich.insert(tk.END,i)
                #Xoa nhung tu co trong listbox nguon
                index = self.TakeValueListBoxLeft().index(i)
                self.textbox_nguon.delete(index)
        else:
            #Dua lai du lieu goc ban dau.
            pass
    #Lua cho list box lam sach
    
    
    #
    def Move_All_Right(self):
        for i in self.TakeValueListBoxLeft():
            if (not(i in self.TakeValueListBoxRight())):
                self.textbox_dich.insert(tk.END,i)
        self.textbox_nguon.delete(0,tk.END)
    def Move_All_Left(self):
        for i in self.TakeValueListBoxRight():
            if (not(i in self.TakeValueListBoxLeft())):
                self.textbox_nguon.insert(0,i)
        self.textbox_dich.delete(0,tk.END)
    def RemoveListBox(self):
        pass
        '''left = 0
        left= self.textbox_dich.curselection()
        right = 0
        right = self.textbox_nguon.curselection()
        if(left!=0):
            self.textbox_nguon.delete(0,tk.END)
        elif(right!=0):
            self.textbox_dich.delete(0,tk.END)'''
        
    
    
        
    #Ham lay cac cac phan tu dong trong listbox left va right    
    def TakeValueListBoxLeft(self):
        return list(self.textbox_nguon.get(0,self.textbox_nguon.size()))
    def TakeValueListBoxRight(self):
        return list(self.textbox_dich.get(0,self.textbox_dich.size()))
        
    def Copy_To_Left(self):
        i = 0
        CongDo08_013 = self.textbox_nguon.curselection() # lấy ds các vị trí chọn
        for i in reversed(CongDo08_013):
            if( not (self.textbox_nguon.get(i) in self.TakeValueListBoxRight())):
                self.textbox_dich.insert(tk.END, self.textbox_nguon.get(i))
    def Move_To_Left(self):
        i = 0
        CongDo08_013 = self.textbox_nguon.curselection() # lấy ds các vị trí chọn
        for i in reversed(CongDo08_013):
            #print(i)
            #print(self.TakeValueListBoxRight())
            if( not (self.textbox_nguon.get(i) in self.TakeValueListBoxRight())):
                self.textbox_dich.insert(tk.END, self.textbox_nguon.get(i))
                self.textbox_nguon.delete(i)
    def RemoveLeft(self):
        i = 0
        CongDo08_013 = self.textbox_nguon.curselection() # lấy ds các vị trí chọn
        for i in reversed(CongDo08_013):
            self.textbox_nguon.delete(i)
    def ButtonLeft(self,e):
         if self.textbox_nguon.size() > 0 :
            Cong08_21133013 = tk.Menu(self.textbox_nguon, tearoff = tk.FALSE)
            Cong08_21133013.add_command(label = "Copy To Left",command=self.Copy_To_Left)
            Cong08_21133013.add_command(label = "Move To Left",command=self.Move_To_Left)
            Cong08_21133013.add_command(label = "Remove",command=self.RemoveLeft)
            Cong08_21133013.tk_popup(e.x_root, e.y_root)
            
    def Copy_To_Right(self):
        i = 0
        CongDo08_013 = self.textbox_dich.curselection() # lấy ds các vị trí chọn
        for i in reversed(CongDo08_013):
            if( not (self.textbox_dich.get(i) in self.TakeValueListBoxLeft())):
                self.textbox_nguon.insert(0, self.textbox_dich.get(i))
    def Move_To_Right(self):
        i = 0
        CongDo08_013 = self.textbox_dich.curselection() # lấy ds các vị trí chọn
        for i in reversed(CongDo08_013):
            if( not (self.textbox_dich.get(i) in self.TakeValueListBoxLeft())):
                self.textbox_nguon.insert(0, self.textbox_dich.get(i))
                self.textbox_dich.delete(i)
    def RemoveRight(self):
        i = 0
        CongDo08_013 = self.textbox_dich.curselection() # lấy ds các vị trí chọn
        for i in reversed(CongDo08_013):
            self.textbox_dich.delete(i)
    def ButtonRight(self,e):
         if self.textbox_nguon.size() > 0 :
            Cong08_21133013 = tk.Menu(self.textbox_nguon, tearoff = tk.FALSE)
            Cong08_21133013.add_command(label = "Copy To Right",command=self.Copy_To_Right)
            Cong08_21133013.add_command(label = "Move To Right",command=self.Move_To_Right)
            Cong08_21133013.add_command(label = "Remove",command=self.RemoveRight)
            Cong08_21133013.tk_popup(e.x_root, e.y_root)
    
    
    
            
    def checkbox_event(self,choice):
        pass
    def Context_Source(self,dl_cot:list,info,listboxHT,entry_of_frame_text_two):
        #self.textbox_nguon
        #self.textbox_nguon.configure(listvariable=dl_cot)
        self.entry_of_frame_text_two = entry_of_frame_text_two
        self.listbox2 = listboxHT
        self.df = info
        for i in dl_cot:
            self.textbox_nguon.insert(tk.END,i)
        #Luu lai thuoc tinh goc ban dau
        self.bs_thuoctinh_goc = self.TakeValueListBoxLeft()
    def Context_Destinate(self):
        pass
#Lop chua text
class FrameText(customtkinter.CTkFrame): #Chua text
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        #self.ldulieutho=customtkinter.CTkLabel(self,text="",text_color='green' ,fg_color= "transparent",corner_radius=10)
        #self.ldulieutho.grid(row=0,column=0)
        #self.my_text= customtkinter.CTkTextbox(self,width=800, corner_radius=0,scrollbar_button_hover_color='dark_color')
        #self.my_text.grid(sticky="nsew")
        #self.my_text.insert("0.0", "This is a text!\n" * 20)
    def InsertDataGridView(self,columns,data):
        self.Clear()
        self.datagrid=Datagrid(self)
        self.datagrid.ThucHien(len(columns),columns,data)
    def InsertContentBegin(self,title,info):
        self.ldulieutho.configure(text = title)
        self.my_text.insert("0.0",info)
    def InsertContentAdd(self,info):
        self.my_text.insert(tk.END,info)    
    def Clear(self):
        for widget in self.winfo_children():
            widget.destroy()



#Infozcore
class FrameInfoZcore(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure(10, weight=10)
        self.attribute_window=None 
        self.bieudo_window=None
        self.optionmenu_var_z = tk.StringVar()
        self.optionmenu = customtkinter.CTkOptionMenu(self, values=["Tính Toán Ma Trận z-core", "Lựa chọn ngưỡng từ biểu đồ", "Đầu ra giá trị"],
                                         command=self.optionmenu_z_core, variable=self.optionmenu_var_z)
        self.optionmenu.set("Tính Toán Ma Trận z-core")
        self.optionmenu.grid(row=5, column=0, padx=20, pady=10)
    def optionmenu_z_core(self,choice):
        if(choice=="Tính Toán Ma Trận z-core"):
            z=self.dl.ZCORES_matran()
            #print(z)
            self.textbox2.InsertDataGridView(list(z.columns),z)
        elif(choice=="Đầu ra giá trị"):
            self.bieudo_window.HienThiNoiDung()
            print("OK")
        elif(choice=="Lựa chọn ngưỡng từ biểu đồ"):
            if self.bieudo_window is None or not self.bieudo_window.winfo_exists():
                self.bieudo_window =  BieuDoWindow(self)  # create window if its None or destroyed
                self.bieudo_window.insertdata(self.df,self.listbox,self.textbox)
                self.bieudo_window.display()
                self.bieudo_window.focus()
            else:
                self.bieudo_window.focus()
        else:
            pass
    def InsertData(self,list_data,data,df,listbox,textbox):
        self.textbox2=list_data
        self.dl=data
        self.df=df
        self.listbox=listbox
        self.textbox = textbox
        print("OK")
#customtkinter.CTk
class Z_CoreWindowCH(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("1600x350")
        self.title("Z-cores")
        self.grid_rowconfigure(10, weight=10)  # configure grid system
        self.grid_columnconfigure(2, weight=10)
        self.maxsize(1600, 450)
        self.minsize(1600, 350)
        self.toplevel_window=None
        
        
    def display(self):
        self.frame_text = FrameText(master=self)
        self.frame_text.grid(row=1, column=1, rowspan=2, columnspan=3 ,padx=20, pady=20, sticky="nsew")
        #self.label_of_frame_text = customtkinter.CTkLabel(self, text="Shape:", fg_color="transparent",font=('Roboto',16))
        #self.label_of_frame_text.grid(row=5,column=1,padx=20,sticky="nsew")
        self.entry_of_frame_text_one = customtkinter.CTkEntry(self, placeholder_text="...")
        self.entry_of_frame_text_one.grid(row=5, column=1,padx=20,sticky="nsew")
        
        self.frame_info = FrameInfoZcore(master=self)
        self.frame_info.grid(row=1, column=0, rowspan=6,padx=20, pady=20, sticky="nsew") 
        self.VeBang()
    
    def VeBang(self):
        dl=self.df.GiaTriChuanHoa4()
        self.frame_text.InsertDataGridView(list(dl.columns),dl)
        self.entry_of_frame_text_one.delete(0,tk.END)
        self.entry_of_frame_text_one.insert(0,f"{dl.shape}")
        self.frame_info.InsertData(self.frame_text,self.df,self.df2,self.listbox,self.textbox)#Dua usercontrol vao
       
    def InsertData(self,data,listbox2,df,textbox):
        self.df = data   
        self.listbox=listbox2
        self.df2 = df
        self.textbox = textbox
#Lop chua info        
class FrameInfo(customtkinter.CTkFrame): #Chua text
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure(12, weight=10)
        self.attribute_window=None 
        self.zcore_window=None
        self.eda_window=None
        self.my_image = customtkinter.CTkImage(light_image=Image.open("./EDA/Logo2.0.PNG"),
                                  dark_image=Image.open("./EDA/Logo2.0.PNG"),
                                  size=(150, 150))
        self.label_icon = customtkinter.CTkLabel(self,image=self.my_image,text="")
        self.label_icon.grid(row=0,column=0)
        #button = customtkinter.CTkButton(app, image=my_image)
        self.button1 = customtkinter.CTkButton(self,text="Bỏ Thuộc Tính",command=self.CollectionAttribute)
        self.button1.grid(row=4, column=0, padx=20, pady=10)
        #self.button2 = customtkinter.CTkButton(self)
        #self.button2.grid(row=5, column=0, padx=20, pady=10)
        self.optionmenu_var = tk.StringVar()
        self.optionmenu = customtkinter.CTkOptionMenu(self, values=["Deleting Rows", "Replacing_Mean","Assigning_Unique"],
                                         command=self.optionmenu_callback, variable=self.optionmenu_var)
        self.optionmenu.set("Deleting Rows")
        
        self.optionmenu.grid(row=5, column=0, padx=20, pady=10)
        self.button3 = customtkinter.CTkButton(self,text="Chuẩn Hóa Thuộc Tính",command=self.CollectionAttributeCH)
        self.button3.grid(row=6, column=0, padx=20, pady=10)
        #self.button4 = customtkinter.CTkButton(self,text="Ma Trận Z-Core")
        #self.button4.grid(row=7, column=0, padx=20, pady=10)
        
        self.bieudo_window = None
        #self.optionmenu_var_z = tk.StringVar()
        #self.optionmenu = customtkinter.CTkOptionMenu(self, values=["Tính Toán Ma Trận z-core", "Lựa chọn ngưỡng từ biểu đồ", "Đầu ra giá trị"],
        #                                 command=self.optionmenu_z_core, variable=self.optionmenu_var_z)
        #self.optionmenu.set("Tính Toán Ma Trận z-core")
        self.button4 = customtkinter.CTkButton(self,text="Z-core",command=self.z_core)
        self.button4.grid(row=7, column=0, padx=20, pady=10)
        #self.optionmenu.grid(row=7, column=0, padx=20, pady=10)
        self.button5 = customtkinter.CTkButton(self,text="Min-Max Scaling",command=self.Min_MaxScaling)
        self.button5.grid(row=8, column=0, padx=20, pady=10)
        self.button6 = customtkinter.CTkButton(self,text="XD thuộc tính đặc trưng",command=self.EDA)
        self.button6.grid(row=9, column=0, padx=20, pady=10)
        self.button7 = customtkinter.CTkButton(self,text="XD mô hình trích lọc",command=self.MoHinhTrichLoc)
        self.button7.grid(row=10, column=0, padx=20, pady=10)
    
    def MoHinhTrichLoc(self):
        self.VeBang(self.df.MINMAXSCALER()[self.df.ThuocTinhTrichLoc()])
    
    def EDA(self):
        
        if self.eda_window is None or not self.eda_window.winfo_exists():
            self.eda_window = EDAWindowCH(self)  # create window if its None or destroyed
            
            self.eda_window.DuLieuAttribute(self.df)
            self.eda_window.display()
            self.eda_window.DuLieuAttribute()
            self.eda_window.focus()
            
        else:
            self.eda_window.focus()  # if window exists focus it
        
    def Min_MaxScaling(self):
        dl = self.df.MINMAXSCALER()
        #print(dl)
        self.VeBang(self.df.MINMAXSCALER())
        
    def z_core(self):
        if self.zcore_window is None or not self.zcore_window.winfo_exists():
            self.zcore_window = Z_CoreWindowCH(self)  # create window if its None or destroyed
            #try:
            self.zcore_window.InsertData(self.df,self.listbox2,self.df,self.textbox)               
            #except:
            #    pass
            self.zcore_window.display()
            self.zcore_window.focus()
            #self.attribute_window.Context_Source(self.attribute,self.df,self.listbox2,self.textbox)
            
        else:
            self.zcore_window.focus()  # if window exists focus it
    def CollectionAttribute(self):
        if self.attribute_window is None or not self.attribute_window.winfo_exists():
            self.attribute_window = AttributeWindow(self)  # create window if its None or destroyed
            self.attribute_window.focus()
            self.attribute_window.Context_Source(self.attribute,self.df,self.listbox2,self.textbox)
            
        else:
            self.attribute_window.focus()  # if window exists focus it
    def DuLieuThuocTinh(self,attribute):
        self.attribute=attribute
        print(self.attribute)
        
    def VeBang(self,dl):
        self.listbox2.InsertDataGridView(list(dl.columns),dl)
        self.textbox.delete(0,tk.END)
        self.textbox.insert(0,f"{dl.shape}")
    def optionmenu_callback(self,choice):
        #Hien thi ra khung lua chon
        #print("optionmenu dropdown clicked:", choice)
        #print(self.df.GiaTriChuanHoa())
        #Dong y xu ly nhan yes, khong nhan no
        if(choice=="Deleting Rows"):
            self.data = self.df.XuLyDuLieu(0)
            self.VeBang(self.data)
        elif(choice == "Replacing_Mean"):
            self.data = self.df.XuLyDuLieu(2)
            self.VeBang(self.data)
        elif(choice == "Assigning_Unique"):
            self.data = self.df.XuLyDuLieu(1)
            self.VeBang(self.data)
        self.listbox2.InsertDataGridView(list(self.data.columns),self.data)
        
    def CollectionAttributeCH(self):
        if self.attribute_window is None or not self.attribute_window.winfo_exists():
            self.attribute_window = AttributeWindowCH(self)  # create window if its None or destroyed
            try:
                self.attribute_window.DuLieuAttribute(self.data,self.listbox2,self.df)
            except:
                pass
            self.attribute_window.display()
            self.attribute_window.focus()
            #
            
        else:
            self.attribute_window.focus()  # if window exists focus it    
    
    def InsertData(self,info):#Day la noi luu tru bien du lieu
        self.df = info
    def InsertControl(self,listbox_TH,textbox2):#Truyen tham so la list_textbox
        self.listbox2=listbox_TH
        self.textbox =textbox2         
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1600x650")
        self.title("G408ĐỗNCCông_googleplaystore_21133013")
        self.grid_rowconfigure(10, weight=10)  # configure grid system
        self.grid_columnconfigure(2, weight=10)
        self.maxsize(1600, 650)
        self.minsize(1600, 600)
        self.troLy=None
        self.toplevel_window=None
        #Create a menu
        self.menubar = tk.Menu(self)
        self.config(menu=self.menubar)
        
        self.file_menu = tk.Menu(self.menubar, tearoff=False)
        self.file_menu.add_command(label='Open File',command=self.PathFile)
        self.file_menu.add_command(label='Save File')
        self.file_menu.add_command(label='Tro Ly', command=self.TroLy)
        self.menubar.add_cascade(label="File",menu=self.file_menu)
        self.menubar.add_cascade(label="Setting",menu=self.file_menu)
        
        #
        
        self.frame_text = FrameText(master=self)
        self.frame_text.grid(row=1, column=1, rowspan=2, columnspan=3 ,padx=20, pady=20, sticky="nsew")
        #self.label_of_frame_text = customtkinter.CTkLabel(self, text="Shape:", fg_color="transparent",font=('Roboto',16))
        #self.label_of_frame_text.grid(row=5,column=1,padx=20,sticky="nsew")
        self.entry_of_frame_text_one = customtkinter.CTkEntry(self, placeholder_text="...")
        self.entry_of_frame_text_one.grid(row=5, column=1,padx=20,sticky="nsew")
        
        
        
        self.frame_text2 = FrameText(master=self)
        self.frame_text2.grid(row=6, column=1, rowspan=2, columnspan=3 ,padx=20, pady=20, sticky="nsew")
        self.entry_of_frame_text_two = customtkinter.CTkEntry(self, placeholder_text="...")
        self.entry_of_frame_text_two.grid(row=9, column=1,padx=20,sticky="nsew")
        
        self.frame_info = FrameInfo(master=self)
        self.frame_info.grid(row=1, column=0, rowspan=6,padx=20, pady=20, sticky="nsew")
        
        #self.frame_text.InsertContentBegin("Hello \n"*20)
        #self.button = customtkinter.CTkButton(self.frame_text)
        #self.button.grid(row=0, column=2, padx=20, pady=10)
    def TroLy(self):
        if self.troLy is None or not self.troLy.winfo_exists():
            self.troLy = AppTroLy()  # create window if its None or destroyed
            self.troLy.TruyenGiaTri(self)    
            self.troLy.Display()
            self.troLy.focus() 
        else:
            self.troLy.focus() 
    def PathFile(self):
        self.filepath = filedialog.askopenfilename(title = "OpenFile", filetypes = (("Text File (.txt)", "*.txt"),("CSV File (.csv)", "*.csv"),("All File (.)", "*")))
        print(self.filepath)
        self.OpenFile()
        #return filepath
    def OpenFile(self):
        #Mo file co dau TV encoding="utf-8"
        #data = dp.read_csv(self.filepath)
        #self.frame_text.InsertContentBegin("Dữ Liệu Thô Ban Đầu:",f"Path of File: {self.filepath}\n")
        #Nap noi dung file vao label text
        #self.frame_text.InsertContentAdd(data)
        self.dl = DuLieu(self.filepath)
        self.frame_info.InsertData(self.dl)
        self.frame_info.InsertControl(self.frame_text2,self.entry_of_frame_text_two)
        self.columns = self.dl.DanhSachCot()
        self.frame_text.InsertDataGridView(self.columns,self.dl.GiaTri())
        self.entry_of_frame_text_one.delete(0,tk.END)
        self.entry_of_frame_text_one.insert(0,f"{self.dl.GiaTri().shape}")
        self.frame_info.DuLieuThuocTinh(list(self.dl.GiaTri().columns))
    #option menu
    def optionmenu_callback(choice):
        #print("optionmenu dropdown clicked:", choice)
        pass
    #Create addition windows
    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it
    
    
if __name__ == "__main__":
    app = App()
    #app=Z_CoreWindowCH()
    app.mainloop()