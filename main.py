# 这是一个示例 Python 脚本。
import os
import subprocess

import pytest

from scripts import test_login


# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 ⌘F8 切换断点。


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    pytest.main()
    print("运行完成")
    # 执行allure generate 生成静态html报告
    # 读取 report 目录下结果，输出到 allure-report，先清空旧报告
    subprocess.run(["allure", "generate", "report", "-o", "allure-report", "--clean"])
    # subprocess.run(["allure", "open", "allure-report"])

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
