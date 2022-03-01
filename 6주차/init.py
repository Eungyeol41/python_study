# 클래스 선언
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def s_name(self):
        return "{}".format(self.name)
    
    def s_age(self):
        return "{}".format(self.age)

    def to_string(self):
        return "{}\t{}".format(self.s_name(), self.s_age())
    
# 학생 리스트 선언
students = [
    Student("Hon", 20),
    Student("Gong", 24),
    Student("Python", 30)
]

# 학생의 이름을 한 명씩 나타냅니다.
print("이름\t나이")
for student in students:
    # 출력
    print(student.to_string())
    