import os

name = "python 换源工具"        # 模块名称
author = "yfblock"             # 作者
introduction = "python 换源工具" # 模块介绍

# 镜像源列表
sources = [
    'http://mirrors.tencentyun.com/pypi/simple',
    'https://mirrors.aliyun.com/pypi/simple',
    'https://pypi.douban.com/simple',
    'https://pypi.mirrors.ustc.edu.cn/simple/',
    'https://pypi.tuna.tsinghua.edu.cn/simple'
]

# 镜像信息
def use_mirror(index):
    os.system('pip config set global.index-url {0}'.format(sources[index]))