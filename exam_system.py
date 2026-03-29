# 定义考试系统
import os
import time
import random
from datetime import datetime
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
        # 静态方法：校验学号格式的合法性
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
        # 读取文本文件并初始化学生列表
        try:
            # 检查文件是否存在
            if not os.path.exists(self.data_file):
                # 异常
                raise FileNotFoundError(f"文件 {self.data_file} 不存在")

            # 打开文件
            with open(self.data_file, 'r', encoding='utf-8') as f:
                # 逐行读取文件内容
                lines = f.readlines()

                # 遍历每一行数据
                for line in lines:
                    # 去除行尾换行符和首尾空格
                    line = line.strip()
                    # 跳过空行
                    if not line:
                        continue
                    # 跳过包含表头关键词的行，防止误读
                    if "姓名" in line or "学号" in line or "序号" in line:
                        continue

                        # 此处假设文件格式为空格分隔
                    parts = line.split()

                    # 确保数据列数足够
                    if len(parts) >= 5:
                        # 创建 Student 对象
                        student = Student(
                            stu_id=parts[0].strip(),
                            name=parts[1].strip(),
                            gender=parts[2].strip(),
                            class_name=parts[3].strip(),
                            college=parts[4].strip()
                        )
                        self.students.append(student)

            # 打印加载人数
            print(f"[数据加载] 成功读取 {len(self.students)} 名学生信息")

        except FileNotFoundError as e:
            # 异常
            print(f"[错误] 无法找到数据文件：{e}")
            print("[提示] 请确保 '人工智能编程语言学生名单.txt' 在同一目录下")
        except Exception as e:
            # 异常
            print(f"[错误] 读取文件时发生未知异常：{e}")

    def find_student(self, stu_id):
        # 根据学号查找学生对象

        # 遍历学生列表
        for student in self.students:
            # 比对学号属性
            if student.stu_id == stu_id:
                return student  # 找到则返回对象
        return None  # 遍历结束未找到，返回 None

    def search_and_print(self, stu_id):
        # 查找与打印

        # 调用查找方法
        result = self.find_student(stu_id)

        # 判断结果是否为空
        if result:
            # 找到学生
            print("\n--- 学生信息 ---")
            print(result)
            print("----------------\n")
        else:
            # 未找到学生时
            print(f"\n[提示] 未找到学号为 '{stu_id}' 的学生信息，请检查输入是否正确。\n")

    def random_pick(self, count):
        # 随机抽取指定数量的学生且不重复

        # 异常
        try:
            total = len(self.students)
            # 数量不能超过总人数
            if count > total:
                raise ValueError(f"抽取数量 ({count}) 不能超过总人数 ({total})")
            # 数量必须大于 0
            if count <= 0:
                raise ValueError("抽取数量必须大于 0")

            # 不重复抽取
            selected_students = random.sample(self.students, count)
            return selected_students

        except ValueError as e:
            # 逻辑校验错误
            print(f"[错误] 点名参数无效：{e}")
            return []
        except Exception as e:
            # 其他未知异常
            print(f"[错误] 点名过程发生未知异常：{e}")
            return []

    def run_roll_call(self, count):
        # 点名并打印结果

        # 获取名单
        result_list = self.random_pick(count)

        # 如果结果为空直接返回
        if not result_list:
            return

        print(f"\n=== 随机点名结果 ({count} 人) ===")
        # 遍历结果列表并打印
        for idx, student in enumerate(result_list, 1):
            print(f"{idx}. {student.name} ({student.stu_id})")
        print("================================\n")

    def generate_exam_table(self):
        # 生成考场安排表文件

        output_file = "考场安排表.txt"

        # 异常
        try:
            # 确保学生数据已加载
            if not self.students:
                raise ValueError("当前没有学生数据，无法生成安排表")

            # 将全班学生顺序随机打乱
            shuffled_students = self.students[:]
            random.shuffle(shuffled_students)

            # 获取当前生成时间
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # 写入文件
            with open(output_file, 'w', encoding='utf-8') as f:
                # 生成时间
                f.write(f"生成时间：{current_time}\n")

                # 写入表头
                f.write(f"{'座位号':<10}{'姓名':<10}{'学号':<15}\n")

                # 遍历打乱后的学生列表，写入座位信息
                for index, student in enumerate(shuffled_students, 1):
                    line = f"{index:<10}{student.name:<10}{student.stu_id:<15}\n"
                    f.write(line)

            # 生成成功后提示
            print(f"[成功] 考场安排表已生成：{os.path.abspath(output_file)}")

        except ValueError as e:
            # 逻辑错误
            print(f"[错误] 生成安排表失败：{e}")
        except PermissionError as e:
            # 权限错误
            print(f"[错误] 无权限写入文件：{e}，请检查文件是否被打开")
        except Exception as e:
            # 其他未知异常
            print(f"[错误] 生成安排表时发生未知异常：{e}")

    def generate_admission_tickets(self):
        pass
