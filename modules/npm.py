import os

name = "npm 换源工具"        # 模块名称
author = "ss"             # 作者
introduction = "npm 换源工具" # 模块介绍

# 镜像源列表
sources = [
    'https://registry.npmmirror.com/',
    'https://registry.npmjs.org'
]

# 镜像信息
def use_mirror(index):
    os.system('npm config set registry={0}'.format(sources[index]))
    print('本工具将对 electron 进行换源')
    os.system('npm config set electron_mirror "{0}"electron/'.format(sources[index]))
