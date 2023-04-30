import pkgutil
import importlib
import modules

# print introduction
print()
print("{:=^40}".format(' 快速换源工具，减少搜索工具的时间 '))
print("{:=^40}".format(' Quickly switch the mirror tool to save the time on the browser '))
print()

# load the module(tools) list
# 获取模块(工具)列表
support_modules = []

for filefiner, name, ispkg in pkgutil.iter_modules(modules.__path__):
    if ispkg:
        continue
    module = importlib.import_module('modules.' + name)
    
    # 如果没有作者信息，则直接替换为空
    if not hasattr(module, 'author'):
        setattr(module, 'author', '')

    # 如果没有在模块内部重定义模块名称，则用文件名作为模块名称
    if not hasattr(module, 'name'):
        setattr(module, 'name', name)

    # 如果没有模块介绍，则直接替换为空
    if not hasattr(module, 'introduction'):
        setattr(module, 'introduction', name)
    
    # 加入模块列表
    support_modules.append(module)


print("请从下列工具中选择一项:")
for i, module in enumerate(support_modules, start=1):
    print('{0}: {1} (Author: {2})'.format(i, module.name, module.author))

index = input('请输入工具前的序号: ')
index = int(index) - 1

if index >= len(support_modules):
    print("请选择有效的工具")
    exit(-1)

selected_module = support_modules[index]

print('工具介绍: {0}'.format(selected_module.introduction))

# 显示镜像源中的信息
print("请在下面的镜像源中选择一个: ")
for i, source in enumerate(selected_module.sources, start=1):
    print('{0}: {1}'.format(i, source))

# get the index of mirror
# 获取镜像的索引
index = input('请输入镜像前的序号: ')
index = int(index) - 1

selected_module.use_mirror(index)
