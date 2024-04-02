import numpy as np 
import pandas as pd 
from scipy import stats 
from sklearn import preprocessing 
from sklearn.feature_selection import SelectKBest, chi2 
import copy
import math


pd.set_option('display.max_columns',None)
class DuLieu:
    def __init__(self,pathfile):
        self.df = pd.read_csv(pathfile)
        #print("Du lieu ban dau",self.df.shape)
        self.df_bs = copy.deepcopy(self.df)
        self.anhxa_thongtin = {}
    def GiaTri(self):
        return self.df
    def GiaTriChuanHoa(self):
        return self.df_bs
    def GiaTriChuanHoa2(self):
        return self.df_bs_2
    def GiaTriChuanHoa3(self):
        return self.df_bs_3
    def GiaTriChuanHoa4(self):#Du lieu zcore
        return self.df_bs_4
    def GiaTriChuanHoa5(self):#Gia tri duoc luu trong zcore
        return self.df_bs_5
    def GiaTriChuanHoa6(self):
        return self.df_bs_6
    def GiaTriChuanHoa7(self):#MinMaxScaling
        return self.df_bs_7
    def CotChuanHoa(self):
        return self.df_bs_qt
    def ThuocTinhTrichLoc(self):
        return self.trichloc
    
    def LoaiBoThuocTinh(self,list_attribute:list): #Loai bo thuoc tinh khong can thiet
        self.df_bs = copy.deepcopy(self.df)
        try:
            self.df_bs.drop(list_attribute, axis='columns',inplace=True)
            #print(self.df_bs)
        except:
            print("Xoa bo cot bi loi")
        
        return self.df_bs
    #Tra ve thong tin cac cot co gia tri rong.
    def CotCoGiaTriRong(self):
        return self.df.columns[self.df.isnull().any()]
    
    
    
    #Tra ve thong tin cac anh xa.
    def ThongTinAnhXa(self):
        return self.anhxa_thongtin
    
    #Chuan hoa sang so, tra ve tap danh sach cac gia tri, va cac gia tri danh dau tuong ung
    def ChuanHoaSo(self,attribute):
        print("ChuanHoaSo")
        self.result = list(self.df_bs_3[attribute].drop_duplicates())
        #print(self.result)
        self.anhxa_thongtin[attribute]=self.result
        for i in range(0,len(self.result)):
            self.df_bs_3[attribute].replace(self.result[i], i+1, inplace=True)
        self.df_bs_4=copy.deepcopy(self.df_bs_3)
        print(self.df_bs_4)
        return self.result
    
    def XuLyDuLieu(self,index:int):# Loai bo cot null, hoac thay the cac gia tri can thiet.
        self.df_bs_2 = copy.deepcopy(self.df_bs)
        if (index==0): #Loai bo cac dong chua gia tri null
            self.df_bs_2 = self.df_bs_2.dropna(how='any')
        elif (index==1): #Them gia tri dau tien tuy vao thuoc tinh neu no rong
            for i in list(self.DanhSachCot()):
                self.df_bs_2[i] = self.df_bs_2[i].fillna(self.df_bs_2[i][0])
        elif (index==2): #Them gia tri giua tuy vao thuoc tinh rong.
            for i in list(self.DanhSachCot()):
                self.df_bs_2[i].fillna(self.df_bs_2[i][int(len(list(self.df_bs_2[i]))//2)],inplace=True)
        else:
            pass
        self.df_bs_3 = copy.deepcopy(self.df_bs_2)
        return self.df_bs_2
    # Tra ve danh sach cot.
    def DanhSachCot(self):
        return list(self.df_bs.columns)
    
    
    #Ma trạn zcore
    def ZCORES_matran(self,giatrimin=0,giatrimax=5):
        self.df_bs_5 = copy.deepcopy(self.df_bs_4)
        print(self.df_bs_5)
        z=np.abs(stats.zscore(self.df_bs_5._get_numeric_data()))
        print(z)
        return z[z[(giatrimin<z)] < giatrimax]
    
    # Tinh Toan du lieu z-core
    def ZCORES(self,giatrimin=0,giatrimax=5):
        #print(self.df_bs._get_numeric_data())
        self.df_bs_6 = copy.deepcopy(self.df_bs_4)
        z=np.abs(stats.zscore(self.df_bs_6._get_numeric_data()))
        #print('Hien thi gia tri z-cores',z)
        self.df_bs_6=self.df_bs_6[(z[(giatrimin<z)] < giatrimax).all(axis=1)]
        #print('Hien thi gia tri z-corse < 0.17',(z < 1).all(axis=1))
        #print('Du lieu sau khi dung z-core la:',self.df_bs.shape)
        print(self.df_bs_6)
        return z, self.df_bs_6
    
    # Tinh Toan Min-Max Scalar
    
    def MINMAXSCALER(self):
        self.df_bs_7 = copy.deepcopy(self.df_bs_6)
        scaler = preprocessing.MinMaxScaler()
        scaler.fit(self.df_bs_7._get_numeric_data())
        self.df_bs_7 = pd.DataFrame(scaler.transform(self.df_bs_7._get_numeric_data()),index=self.df_bs_7.index,  columns=self.df_bs_7.columns)
        print('Du lieu scaler',self.df_bs_7)
        return self.df_bs_7
    
    #
    def ChuanHoaKhongMot(self,giatri):
        if(giatri<0.5):
            return math.floor(giatri)
        return math.ceil(giatri)
    # Tinh toan EDA
    def EDA(self,attribute_target,k_value):
        #print("EDA")
        self.df_bs_qt = copy.deepcopy(self.df_bs_7)
        self.df_bs_qt[attribute_target] = [self.ChuanHoaKhongMot(i) for i in self.df_bs_qt[attribute_target]]
        X = self.df_bs_qt.loc[:,self.df_bs_qt.columns!=attribute_target]
        #X=self.df_bs_qt[self.df_bs.columns]
        #print(X)
        y = self.df_bs_qt[[attribute_target]]
        #print(y)
        select = SelectKBest(chi2, k=k_value)
        select.fit(X, y)
        #print(select)
        select.transform(X)
        #z = select.fit_transform(X,y)
        #print(X_new.shape)
        #print(X_new)
        self.trichloc=list(X.columns[select.get_support(indices=True)])
        #return z
        return self.trichloc
    
    def NhuCau(self):
        pass
    def TakeTheListValue(self):
        return self.GiaTri().values.tolist()
if __name__ == '__main__':
    dl = DuLieu("./G408ĐỗNCCông_googleplaystore.csv")
    print(dl.CotCoGiaTriRong())
    #print(dl.GiaTri())
    thongtin=dl.LoaiBoThuocTinh([ 'Rating','App', 'Reviews', 'Genres', 'Last Updated', 'Current Ver', 'Android Ver' ])
    #for i in dl.GiaTri().values.tolist():
    #    print(i)
    print(dl.XuLyDuLieu(2))
    #print(dl.ChuanHoaSo("Category"))#Lay mot tupple de luu thong tin can thiet
    print(dl.GiaTriChuanHoa())
    for i in list(dl.DanhSachCot()):
        dl.ChuanHoaSo(i)
    print(dl.GiaTriChuanHoa())
    #print(dl.ThongTinAnhXa())
    #print(dl.DanhSachCot())
    z,info=dl.ZCORES(2)
    print(info)
    dl.MINMAXSCALER()
    #print(dl.EDA("Installs",3).shape)
    print(dl.EDA("Installs",2))