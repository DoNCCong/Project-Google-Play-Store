import speech_recognition as sr
from gtts import gTTS
import os
import time
import playsound
import customtkinter
import tkinter as tk

customtkinter.set_default_color_theme("dark-blue")
class Assitant:
    def __init__(self,data):
        self.dl = data
        self.Cong08_thoigian=5
        self.cong_r = sr.Recognizer()
        self.Cong_NN='vi'
    def KQ(self):
        return self.collection
    def Menu(self,text):
        '''
        1. Mở file và lựa chọn file
        2. Mở bản loại bỏ thuộc tính
        3. Chuẩn hóa thuộc tính
        4. Z-Core
        5. Min-Max Scaling
        6. Mo Bang XD Thuoc Tinh Dac Trung
        7. XD MoHinhTrichLoc
        '''
        self.collection = 0;
        text = text.lower()
        if '1' or 'một' or 'one' in text:
            self.collection = 1
        if '2' or 'hai' or 'two' in text:
            self.collection = 2
        if '3' or 'ba' or 'three' in text:
            self.collection = 3
        if '4' or 'bốn' or 'four' in text:
            self.collection = 4
        if '5' or 'năm' or 'fine' in text:
            self.collection = 5
        if '6' or 'sáu' or 'sixs' in text:
            self.collection = 6
        if '7' or 'bảy' or 'seven' in text:
            self.collection = 7
        return self.collection
    def Cong08_21133013(self,Cong08_text,Cong_NN): #Phat am thanh
        self.cong_t = time.localtime()
        self.info = str(self.cong_t.tm_year)+str(self.cong_t.tm_mon)+str(self.cong_t.tm_mday)+str(self.cong_t.tm_hour)+str(self.cong_t.tm_min)+str(self.cong_t.tm_sec)
        self.Cong_Ten = gTTS(Cong08_text,lang=Cong_NN)
        self.Cong_08_filename='.\\08DoNgocChiCongMau\\08DoNgocChiCong'+self.info+'.mp3'
        print(self.Cong_08_filename)
        self.Cong_Ten.save(self.Cong_08_filename)  
        try:
            playsound.playsound(self.Cong_08_filename)
        except:
            print("Loi khong tim thay duong dan den file.")
    
    def NgonNgu(self,n):
        self.nNgonNgu = n
        if(self.nNgonNgu == 2):
            self.Cong_NN='en-US'
        else:
            self.Cong_NN='vi'
    
    def ThoiGian(self,n=5):
        self.Cong08_thoigian = n
        
    def ThucThi(self):
        with sr.Microphone() as source:
            #while True:#Chon thoi diem ghi am
            #    if keyboard.read_key() == 'enter':#Nhan Enter de bat dau ghi am
            #        break
            
            #print('Noi di ban'+str(self.Cong08_thoigian)+'s sau minh se in ra Cong08_text:')
            Cong08_audio = self.cong_r.record(source,duration=self.Cong08_thoigian)
            #print('Ket qua nhan dien...')
            try:
                self.Cong08_text=self.cong_r.recognize_google(Cong08_audio,language=self.Cong_NN)
            except:
                self.Cong08_text='Ban noi gi minh khong hieu\n'
            #print('Ban noi la: '+self.Cong08_text)
            
            #self.Cong08_21133013(self.Cong08_text,self.Cong_NN)
            print(self.Menu(self.Cong08_text))
            
    def KetQua(self):
        print(self.Cong08_text)
        return self.Cong08_text
class AppTroLy(customtkinter.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("TroLy_Cong_08")
        self.geometry("400x500")
        self.grid_rowconfigure(10, weight=10)
        self.maxsize(400, 500)
        self.minsize(400, 500)
    def Display(self):
        self.troly = Assitant(None)
        self.CongDo08 = tk.Listbox(self, height = 20, width = 40, font = "Consolas 8")
        #CongDo08.bind("<Button-3>", ShowPopupMenu) #<Button-3> : đăng ký sự kiện cho chuột phải của listbox = e: vị trí
        self.CongDo08.grid(row=0, column=1,padx=90,pady=20)  
        self.CongDo08_Button = customtkinter.CTkButton(self,text="Ghi Âm Và Thưc Thi",command=self.GhiAmVaThucThi_Cong08)
        self.CongDo08_Button.grid(row=4,column=1,padx=90,pady=20)
        self.CongDo08_2113 = tk.StringVar()
        self.C1 = customtkinter.CTkRadioButton(self, text='GiongVN', value='Viet', variable=self.CongDo08_2113)
        self.C1.grid(row=5, column=1,padx=90,pady=20)
        self.C2 = customtkinter.CTkRadioButton(self, text='GiongAnh', value='Anh', variable=self.CongDo08_2113)
        self.C2.grid(row=6, column=1,padx=90,pady=20)
    def ThucHien(self):
        if(self.kq==1):
            self.master.PathFile()
        elif(self.kq==2):
            self.master.frame_info.CollectionAttribute()
        elif(self.kq==3):
            pass
        elif(self.kq==4):
            self.master.frame_info.CollectionAttributeCH()
        elif(self.kq==5):
            self.master.frame_info.Min_MaxScaling()
        elif(self.kq==6):
            self.master.frame_info.EDA()
        elif(self.kq==7):
            self.master.frame_info.MoHinhTrichLoc()
    def GhiAmVaThucThi_Cong08(self):
        self.CongDo08.insert(tk.END,"Bạn nói đi sau năm giây mình sẽ phân tích kết quả.\n")
        if(self.CongDo08_2113.get()=="Anh"):
            self.troly.NgonNgu(2)
        else:
            self.troly.NgonNgu(1)
        self.troly.ThucThi()
        self.kq=self.troly.KQ()
        self.CongDo08.insert(tk.END,self.kq)
        self.ThucHien()
    def KQ(self):
        return self.kq 
    def TruyenGiaTri(self,master):
        self.master=master            
if __name__ == "__main__":
    troly = AppTroLy()
    troly.mainloop()