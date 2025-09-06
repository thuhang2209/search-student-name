# Viết chương trình cho phép người dùng nhập tên n sinh viên → lưu vào file students.txt.
s=open("students.txt","w")
n= int(input("nhap so sinh vien ma ban muon luu tru: "))
for i in range(n):
    name=input("nhap ten sinh vien: ")
    s.write(name + "\n")
s.close()
# Đọc file students.txt và in ra từng tên kèm số thứ tự (1. Hằng, 2. ngo, …).
s=open("students.txt","r")
student=s.readlines()
for index, name in enumerate(student, start=1):
    print(f"{index}. {name.strip()}")
s.close()
# (Nâng cao) Viết thêm chức năng: tìm kiếm 1 sinh viên trong file theo tên.
def timkien(names):
    s=open("students.txt","r")
    students=s.readlines()
    for a in students:
        if names.lower()==a.strip().lower():
            print("tim thay sinh vien:", names)
            break
        else:
            print("khong tim thay sinh vien:", names)
            break
hoten=input("nhap ten ma ban muon tim:")
timkien(hoten)