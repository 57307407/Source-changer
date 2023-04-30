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
    tool_name = input('请输入您要使用的工具(npm、yarn、pnpm):')
    if tool_name not in ['npm', 'yarn', 'pnpm']:
        print('not support this tool: ', tool_name)
        print('不支持当前工具: ', tool_name)
        return
    print(tool_name)
    os.system('{0} config set registry {1}'.format(tool_name, sources[index]))
    print('本工具将对 electron 进行换源')
    os.system('{0} config set ELECTRON_MIRROR "{1}"electron/'.format(tool_name, sources[index]))
