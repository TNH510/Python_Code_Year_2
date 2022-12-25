'''class sv :
    nganh_hoc = "cơ điện tử"
    khoa_hoc = 2020

    def __init__(self,a,b,c): #constuctor
        self.ho_ten = a
        self.mssv = b
        self.tuoi = c 
    def in_thong_tin(self):
        print("---------------------")
        print("self.Họ và tên :",self.ho_ten)
        print('Khóa học',self.khoa_hoc)
        print('Ngành học',self.nganh_hoc)
        print(self.tuoi)
        print(self.mssv)
A = sv(2,25,26)
A.in_thong_tin()
'''




class _10A1 :
    #day la lop 10A1
    def __init__(self,ten,tuoi,gioitinh,diachi ) : 
        self.ten = ten
        self.tuoi = tuoi
        self.gioitinh = gioitinh
        self.diachi = diachi
A1 = _10A1('Tran Ngoc self.Hieu')

print(A1.ten)  




class _11B1 :
    def __init__(self,a,b) :
        self.ten = a  
        self.tuoi = b      
B= _11B1('hieu tran',14)
print(B.ten, B.tuoi)


