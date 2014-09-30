__author__ = 'yiqing'
'''
sys 基本包含底层的os相关信息
'''
import sys

print(sys.platform,sys.maxsize,sys.version)

if sys.platform[:3] == 'win': print('hello win')

##  很重要的一个属性 查找目录根列表 从左到右扫描指定的py文件
print(sys.path)
## 可以手动配置需要扫描的目录：append extend insert pop remove等操作
## 用脚本修改后 其后的执行就会扫描他们的
sys.path.append(r'C:\myDir')
print(sys.path)
## PYTHONPATH 环境变量的效果跟这个差不多
'''
注意上面要用raw 格式的字符串 不然python对反斜杠会转义的
这样你就不得不用\\ 这样搞 很累赘了-》c:\\xx\\xx\\xxx
'''