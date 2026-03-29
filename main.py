# 描述：测试查找功能
from exam_system import ExamSystem
def main():
    # 初始化系统
    system = ExamSystem()

    # 加载数据
    system.load_data()

    # 异常
    if not system.students:
        print("[系统] 由于数据加载失败，无法进行查找测试。")
        return

    # 用户输入
    print("\n=== 学生信息查询系统 ===")
    while True:
        print("1. 查询学生信息")
        print("2. 随机点名")
        print("3. 生成考场安排表")
        print("4. 退出程序")

        # 异常
        try:
            choice = input("请选择功能 (1-4): ").strip()

            if choice == '1':
                # 查询
                stu_id = input("请输入学号：").strip()
                system.search_and_print(stu_id)

            elif choice == '2':
                # 随机点名
                # 异常
                try:
                    input_str = input("请输入需要点名的学生数量：").strip()
                    count = int(input_str)  # 尝试转换为整数
                    system.run_roll_call(count)
                except ValueError:
                    # 转换失败
                    print("[错误] 输入无效：请输入数字字符。\n")
                except KeyboardInterrupt:
                    print("\n[系统] 操作取消。\n")

            elif choice == '3':
                # 调用生成考场安排表功能
                system.generate_exam_table()

            elif choice == '4':
                print("[系统] 退出程序。")
                break
            else:
                print("[提示] 无效的选择，请输入 1-4。\n")

        except KeyboardInterrupt:
            # Ctrl+C 强制退出
            print("\n[系统] 检测到强制退出，程序终止。")
            break
        except Exception as e:
            # 其他异常
            print(f"[系统错误] 发生未知错误：{e}")


if __name__ == "__main__":
    main()
