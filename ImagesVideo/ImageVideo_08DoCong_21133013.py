'''
    Created by 08 Đỗ Ngọc Chí Công.
'''
import customtkinter
import tkinter as tk
import cv2
from tkinter import filedialog
import os


customtkinter.set_default_color_theme("dark-blue")
DoCong08 = customtkinter.CTk()
DoCong08.title("Image_Cong_08")
DoCong08.geometry("400x500")
DoCong08.grid_rowconfigure(10, weight=10)
DoCong08.grid_columnconfigure(2, weight=10)
DoCong08.maxsize(400, 500)
DoCong08.minsize(400, 500)
def DoCong08_CA(DoCong8):
    # CHUYỂN ẢNH =>ẢNH XÁM img
    img = cv2.imread(DoCong8,cv2.IMREAD_GRAYSCALE)
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
#DoCong08_CA("3d floweC1.jpg")
def DoCong08_VF(DoCong8):
    global CongDo21133013
    CongDo21133013 = []
    DC = cv2.VideoCapture(DoCong8)
    count = 0 #biến đếm số khung hình -> bắt đầu từ số 0
    while DC.isOpened(): #trong khi Video clip đang còn phát
        ret,frame = DC.read() #chụp ra một khung hình: khung chụp được lưu vào biến frame;
        #ret = vị trí tiếp theo của Video (sau khung hình vừa chụp)
        cv2.imshow('Khung Hinh', frame) #Hiển thỉ khung hình vừa chụp (ở trên: trong biến frame)
        CongDo21133013.append(f"Khung{count}.jpg")
        cv2.imwrite("./ImageFrame/Khung%d.jpg" %count, frame) #Lưu khung hình này vào file Khung<count>.jpg từ biến frame
        count = count + 1 # tăng chỉ count lên 1 để chuẩn bị lưu khung hình kế tiếp
        if cv2.waitKey(10) & 0xFF == ord('q'): # chờ gõ phím kết thúc là phím q (tránh trường hợp Video quá dài)
            break
    #while sẽ end trong 2 trường hợp: 1 khi NSD gõ q OR khi hết Video Clip hết
    DC.release() #Giải phóng biến đối tượng Video DC
    cv2.destroyAllWindows() # Đóng tất cả các cửa số
    for i in CongDo21133013:
        CongDo08.insert(tk.END,i)
#DoCong08_VF("./HongKong.mp4")
def DC08():
    try:
        global DoNCCong08 # bien toan cuc
        #Hop thoai Mo thu muc
        DoNCCong08 = filedialog.askopenfilename(title = "08 Đỗ Ngọc Chí Công, VideoFrame", filetypes = (("Image File (.jpg)", "*.jpg"),("Video File (.mp4)", "*.mp4")))
        DoNCCong08=DoNCCong08.split("/")[-2]+"/"+DoNCCong08.split("/")[-1]
        #DoNCCong08 = DoNCCong08.split("/")[-1]
    except:
        pass
def ThucThi():
    try:
        if(DoNCCong08!=""):
            path = "./"+DoNCCong08
            if(CongDo08_2113.get() == "Image"):
                print(path)
                DoCong08_CA(path)
            elif (CongDo08_2113.get() == "Video"):
                DoCong08_VF(path)
        print(DoNCCong08)
    except:
        print("Loi trong qua trinh xu ly.")
def DC21133013():
    global DoNCCong08
    DoNCCong08 = "./ImagesVideo/"+"ImageFrame/"+str(CongDo08.get(CongDo08.curselection()[0]))
    print(DoNCCong08)
    DoCong08_CA(DoNCCong08)
def ShowPopupMenu(e):
    if CongDo08.size() > 0 :
        DoNCC08 = tk.Menu(CongDo08, tearoff = tk.FALSE)
        DoNCC08.add_command(label = "Select", command = DC21133013)
        DoNCC08.tk_popup(e.x_root, e.y_root)
DoNChiC08 = customtkinter.CTkButton(DoCong08,text = "Open text File", command = DC08)
DoNChiC08.grid(row=1, column=1,padx=130)
CongDo08_2113 = tk.StringVar()
C1 = customtkinter.CTkRadioButton(DoCong08, text='Chuyen Anh Xam', value='Image', variable=CongDo08_2113)
C1.grid(row=2, column=1,padx=130,pady=20)
C2 = customtkinter.CTkRadioButton(DoCong08, text='Video', value='Video', variable=CongDo08_2113)
C2.grid(row=3, column=1,padx=130,pady=20)
C3 =  customtkinter.CTkButton(DoCong08, text='ThucThi', command=ThucThi)
C3.grid(row=4, column=1,padx=120,pady=20)
CongDo08 = tk.Listbox(DoCong08, height = 20, width = 40, font = "Consolas 8", selectmode =
tk.EXTENDED)
CongDo08.bind("<Button-3>", ShowPopupMenu) #<Button-3> : đăng ký sự kiện cho chuột phải của listbox = e: vị trí
CongDo08.grid(row=5, column=1,padx=90,pady=20)
DoCong08.mainloop()