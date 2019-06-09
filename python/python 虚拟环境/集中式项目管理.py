# 1.0 virtualenvwrapper-win 集中式虚拟环境管理
#     为了结果 virtualenv 虚拟环境 过于分散 每个
#     项目 都有需要创建一个文件夹，而且操作过去繁琐
#     所以 基于 virtualenv 又开发出了 一个 virtualenvwrapper-win
#     
# 2.0  作用
#       他可以将 之前分散的 虚拟环境 集中到一个路径下面进行管理
#      方便虚拟环境之间的切换
#      可以更加方便的去使用virtualenv
#       
# 3.0 --- 创建虚拟环境
#         mkvirtualenv 虚拟环境名称
#         他把所有的虚拟环境 默认创建到 指定的 user/Envs文件里面进行 集中管理
#         -- 他创建完毕 直接就是激活状态
#         -- 他在一个虚拟环境的激活状态下 可以创建下一个虚拟环境
#         
# 4.0 --- 查看所有的虚拟环境
#          lsvirtualenv 查看所有的虚拟环境
#          workon 也可以查看所有的文件列表
#  
# 5.0 --- 切换虚拟环境
#          workon 名称
#      
# 6.0 --- 关闭虚拟环境
#          deactivate 名称
#      
# 7.0 --- 删除虚拟环境
#          rmvirtualenv 名称    