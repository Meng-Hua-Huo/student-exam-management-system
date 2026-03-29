#定义学生数据类，用于封装学生的基本信息
class Student:
    def __init__(self, stu_id, name, gender, class_name, college):
        self.stu_id = stu_id  # 初始化学号
        self.name = name  # 初始化姓名
        self.gender = gender  # 初始化性别
        self.class_name = class_name  # 初始化班级
        self.college = college  # 初始化学院
    def __str__(self):
        # 使用 f-string 输出
        return f"姓名：{self.name}, 学号：{self.stu_id}, 性别：{self.gender}, 班级：{self.class_name}, 学院：{self.college}"
