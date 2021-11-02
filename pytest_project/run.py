'''
@project:python
@Time:2020/9/1 14:39 
@Author:Wyj
@File:run.py.py
'''
import pytest

# # 指定运行单个测试目录
# pytest.main(['./test_case'])
#
# # 指定运行单个测试文件
# pytest.main(['./test_case/test_func.py'])
#
# # 指定运行测试类
# pytest.main(['./test_case/test_func.py::TestFunc'])
#
# # 指定运行测试类中的某个方法
# pytest.main(['./test_case/test_func.py::TestFunc::test_add_by_class'])
#
# # 指定运行单个测试函数
# pytest.main(['./test_case/test_func.py::test_add_by_func_aaa'])

if __name__ == '__main__':
    pytest.main(['--html=./report/test_x.html', './testcase'])


