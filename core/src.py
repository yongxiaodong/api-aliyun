# -*- coding: utf-8 -*-
# @Author: BigHead

from lib import logger



def f1():
    print('登录功能')
    logger.info('登录了')


def f2():
    print('注册功能')
    logger.info('注册了')


def f3():
    print('注销功能')
    logger.info('注销了')


def f4():
    print('退出功能')
    logger.info('退出了')

func_list = {
    "0": ['登录', f1],
    "1": ['注册', f2],
    "2": ['注销', f3],
    "3": ['退出', f4]
}

def run():
    while True:
        print("===================")
        for key in func_list:
            print(key, func_list[key][0])
        u_input = input("请输入:").strip()
        if u_input in func_list:
            func_list[u_input][1]()


if __name__ == "__main__":
    run()
