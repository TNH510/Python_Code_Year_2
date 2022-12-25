#Viết câu lệnh xây dựng hàm Fibonacci(n) với n là số tự nhiên.
#self.Hàm trả về 1 danh sách với các phần tử tương ứng là giá trị của dãy số Fibonacci có n giá trị

def Fibonacci(n) :    
    F = [1,1]
    for i in range(1,n-1):
        F.append(i)
        F[i+1] = F[i] + F[i-1]
    if a == 0 :
        F = []
    if a == 1 :
        F= [1]
    return F

#Nhập và chạy thử
x = input('Mời bạn nhập một số tự nhiên : ')
while x.isdigit() == False : 
    x = input('Mời bạn nhập lại đúng định dạng : ')
a = int(x) 

print('Danh sách',a,'phần tử đầu tiên của dãy Fibonacci :\n',Fibonacci(a))

