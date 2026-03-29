# 定义考试系统
import os
import time
from student import Student  # 导入之前定义的学生类
class ExamSystem:
    def __init__(self, data_file="人工智能编程语言学生名单.txt"):
        # 初始化学生列表
        self.students = []
        # 记录数据文件路径
        self.data_file = data_file
        # 准考证文件夹名称
        self.admission_folder = "准考证"
        # 验证数据文件路径是否合法
        try:
            # 检查路径是否为字符串类型
            if not isinstance(data_file, str):
                raise TypeError("数据文件路径必须是字符串类型")
            # 检查路径是否为空
            if not data_file.strip():
                raise ValueError("数据文件路径不能为空")

            print(f"[系统初始化] 数据文件路径已设定：{data_file}")
        except (TypeError, ValueError) as e:
            # 类型错误或值错误
            print(f"[警告] 文件路径设置异常：{e}，将使用默认路径")
            self.data_file = "人工智能编程语言学生名单.txt"

    @staticmethod
    def validate_student_id(stu_id):
        #静态方法：校验学号格式的合法性
        try:
            # 学号不能为空，且必须是字符串类型
            if not stu_id or not isinstance(stu_id, str):
                return False
            # 去除首尾空格后检查长度
            stu_id = stu_id.strip()
            if len(stu_id) < 5 or len(stu_id) > 20:
                return False

            return True
        except Exception as e:
            # 异常
            print(f"[警告] 学号校验过程发生异常：{e}")
            return False

    def load_data(self):
        pass

    def find_student(self, stu_id):
        pass

    def random_pick(self, count):
        pass

    def generate_exam_table(self):
        pass

    def generate_admission_tickets(self):
        pass
