import pytest

class Test():
    @classmethod
    def setup_module(cls):
        print("------初始化模块cls-------")

    @classmethod
    def teardown_module(cls):
        print("------清除模块cls-------")

    def setup_module(self):
        print("------初始化模块-------")

    def teardown_module(self):
        print("------清除模块-------")


    def test_01(self):
        a = 1
        b = 2
        assert a == b

    def test_02(self):
        a = 1
        b = 1
        assert a == b


