import os
import re
name = "maven 换源工具"        # 模块名称
author = "ss"             # 作者
introduction = "maven 换源工具" # 模块介绍

# 镜像源列表
sources = [
    '阿里云公共仓库',
    '阿里云仓库+中心仓库',
    '还原'
]


sources_list = [
    '''</mirrors>
            <mirror>
                <id>aliyunmaven</id>
                <mirrorOf>*</mirrorOf>
                <name>阿里云公共仓库</name>
                <url>https://maven.aliyun.com/repository/public</url>
            </mirror>
        </mirrors>''',
    '''<mirrors>
            <mirror>
                <id>aliyunmaven</id>
                <mirrorOf>central</mirrorOf>
                <name>阿里云公共仓库</name>
                <url>https://maven.aliyun.com/repository/central</url>
            </mirror>
            <mirror>
                <id>repo1</id>
                <mirrorOf>central</mirrorOf>
                <name>central repo</name>
                <url>http://repo1.maven.org/maven2/</url>
            </mirror>
            <mirror>
                <id>aliyunmaven</id>
                <mirrorOf>apache snapshots</mirrorOf>
                <name>阿里云阿帕奇仓库</name>
                <url>https://maven.aliyun.com/repository/apache-snapshots</url>
            </mirror>
        </mirrors>''',
        '''
        <mirrors>
        </mirrors>
        '''
]

# 镜像信息
def use_mirror(index):
    print("选择操作系统：")
    print("1、windows")
    print("2、Linux")
    choose = int(input('请输入系统的序号: ')) 
    choose = choose - 1 
    if choose > 1:
        print("请选择有效的途径")
        exit(-1)
    if choose == 0:
        print("idea")

    if choose == 1:
        terminal(index)


def terminal(index):
    a = os.popen('mvn -v')
    path = a.read()
    begin = path.find("Maven home:") + 11
    end = path.find("maven") + 5
    path = path[begin:end] + "/conf/settings.xml"
    os.system("chmod 777  "+path)
    a = os.popen('cat '+ path )
    conf = a.read()
    result = re.sub(pattern='<mirrors.*?>(.|\n)*?</mirrors>',string=conf,repl=sources_list[index])
    path = path.strip()
    print (path)
    f = open(path, "w")
    f.write(result)
    f.close()


