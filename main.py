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
        # 异常
        try:
            # 获取用户输入
            user_input = input("请输入学号查询 (输入 q 退出): ").strip()

            # 判断是否退出
            if user_input.lower() == 'q':
                print("[系统] 退出程序。")
                break

            # 调用系统方法查找并打印
            system.search_and_print(user_input)

        except KeyboardInterrupt:
            # Ctrl+C 强制退出
            print("\n[系统] 检测到强制退出，程序终止。")
            break
        except Exception as e:
            # 其他异常
            print(f"[系统错误] 发生未知错误：{e}")


if __name__ == "__main__":
    main()
