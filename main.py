import sys
from search_code import init
from search_code import search

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    search(init(sys.argv[1], sys.argv[2]), sys.argv[3])

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
