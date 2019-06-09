# --- 单文件的安装 通常把这个单文件放到 
#     Python\\Python37-32\\lib\\site-packages'
#     这个文件里面
import sys
print(sys.path)

# --- 安装带有setup.py的文件
#     1.0 打开命令行 工具
#     2.0 切换到setup.py这个文件的目录
#     3.0 python.setup.py install
#         如果在不同的python版本上安装 
#         只需指定python 版本即可
#     4.0 三方包一般储存在 site_packages
#         这个文件夹里面
#         如果卸载 直接把里面的删掉就可以了
#         或者通过 pip包管理器 来进行删除
#         
#     --- 注意 
#         如果你安装的第三方包 是用distutils 库打包的
#         那么我们直接可以安装，因为distutils是系统
#         标准库 一般python自带的有这个库
#         
#         但是如果你安装的三方包 是用 setuptools打包的
#         那么 可能会报错 本地不存在setuptools这个包
#         那么 就需要我们手动的安装这个 库
#         然后在安装 这个三方包
#       
#     --- 安装 setuptool库 
#     
#          1.0 先到pipy平台 下载setuptool这个包
#          2.0 因为 setuptools这个包 是基于 distutils官方标准包 进行打包的
#              所以我们可以直接在 在python上面安装 setuptools
#          3.0 按照 三方包 的安装顺序 进行安装 setuptools
#          
# ---  安装.egg后缀名的包
#      1.0 进入到这个包的路径下
#      2.0 需要已经安装好 setuptools这个包
#      3.0 输入 easy_install 包名  来安装
# --- 安装 .whl后缀名的包
#     也可以使用easy_insatll 这种方式进行安装
#     但是 最新通用的方式 应该 是用pip 包管理器来安装
#     前提是 已经安装pip  在安装python 的时候 应该勾上 pip
#     pip insatll 包名  安装
#     
# --- 注意 在安装包的同时 系统会自动将 包关联的包一起下载 
# 