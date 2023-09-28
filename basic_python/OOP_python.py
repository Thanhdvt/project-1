# Quản lý môn học (các thông tin về sinh viên, giảng viên)
# Sử dụng tính kế thừa thể hiện lớp Lecturer và Student kế thừa các thuộc tính (first_name,last_name,age,email) từ lớp cha Person 
# Sử dụng tính đa hình (ở đây là nạp chồng) để định nghĩa hai phương thức print_info() khác trong hai lớp Student và Lecturer
class Project:
    def __init__(self, name,year,id_number,lecturer):
        self.name = name
        self.year = year
        self.id_number = id_number
        self.lecturer = lecturer
        self.student_list = []

    def enroll(self,student):
        self.student_list.append(student)

    def print_student(self):
        print("----------Students in subject " + self.name + "----------")
        for i in self.student_list:
            txt = "{:<16} {:<16} {:<6d} {:<16}"
            txt2 = "{:<16} {:<16} {:<6} {:<16}"
            print(txt2.format("First name", "Last name", "Age", "Email"))
            print(txt.format(i.first_name, i.last_name, i.age, i.email))
           
    def print_lecturer(self):
        print("\n\n\n----------Lecturer in subject " + self.name + "----------")
        txt = "{:<16} {:<16d}"
        txt2 = "{:<16} {:<16}"
        print(txt2.format("Name", "Bank Account"))
        print(txt.format(self.lecturer.first_name, self.lecturer.bank_account))

class Person:
    def __init__(self, first_name,last_name,age,email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def print_info(self):
        print(self.first_name +" " +self.last_name +" is " + str(self.age) +" years old.")
        print("Email:" + self.email)

class Lecturer(Person):
    def __init__(self,f_name,l_name,age,email,bank_account):
        super().__init__(f_name,l_name,age,email)
        self.bank_account = bank_account
    
    def print_info(self):
        super().print_info()
        print("Bank Account:" + str(self.bank_account))
       
class Student(Person):
    def __init__(self,f_name,l_name,age,email,student_id, grade):
        super().__init__(f_name,l_name,age,email)
        self.student_id = student_id
        self.grade=grade
    
    def print_info(self):
        super().print_info()
        print("Student ID: " + self.student_id)
        print("Grade: " + str(self.grade))
        print()


#Khởi tạo các đối tượng
lecturer = Lecturer("Trung","Bùi Quốc", 35,"trung.buiquoc@hust.edu.vn",1234567)
python_project = Project("Project I",2019,1234,lecturer)
student_Thanh = Student("Thành","Nguyễn Duy", 20,"thanh.nd204691@sis.hust.edu.vn","108001024", "IT1-02")
student_Ba=Student("Ba", "Nguyễn Văn", 21, "banguyen@gmail.com", "108001025", "IT1-03")
python_project.enroll(student_Thanh)
python_project.enroll(student_Ba)

#In ra chi tiết sinh viên và giảng viên có trong đồ án
python_project.print_student()
python_project.print_lecturer()
print("\n\n\n----------Detail Information---------")
student_Thanh.print_info()
student_Ba.print_info()
lecturer.print_info()