import customtkinter
import os


Cong_08 = customtkinter.CTk()
Cong_08.geometry("400x300")
Cong_08.title("App_Cong_08")
Cong_08.grid_rowconfigure(10, weight=10)
Cong_08.grid_columnconfigure(2, weight=10)

def EDA():
    os.system('python "./EDA/G408ĐỗNCCông_googleplaystore.py"')
def ImageVideo():
    os.system('python "./ImagesVideo/ImageVideo_08DoCong_21133013.py"')


button_EDA = customtkinter.CTkButton(Cong_08,text="EDA",command=EDA)
button_EDA.grid(row=1,column=1,padx=130,pady=20)
button_Image = customtkinter.CTkButton(Cong_08,text="Image_Video",command=ImageVideo)
button_Image.grid(row=3,column=1,padx=130,pady=20)


Cong_08.mainloop()