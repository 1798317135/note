# 1.0 pipenv 更加基于项目。推荐使用他来创建虚拟环境
# 
# 2.0 pipenv 是pip 和 virtualenv 的合体
#     他会把 通过项目名称 把项目和 虚拟环境关联起来
#     并且分开 储存
#     他创建的虚拟环境默认是储存在
#     C:\Users\17983\.virtualenvs\
#     文件夹下面
#     并且会在项目里面创建一个 pipfile文件
#     这个文件详细记录 项目管理的 虚拟环境的信息
#     
#     虚拟环境下面会有一个.project 来记录关联的项目的 地址
#     
# 3.0 --- 激活项目
#      pipenv shell 激活项目关联的虚拟环境
#      exit 退出 虚拟环境
#  
# 4.0 --- 安装三方库
# 
#     pipenv 不要用 pip去安装
#     要用他自带的命令去安装
#     
#     --- pipenv install xxx
#         这个命令会把三方包安装在 项目的虚拟环境下
#         的 lib/site-packages
#         并且会在项目中生成 一个pipfile.lock文件
#         这个文件详细记录 安装这个包 所依赖的 包 的全部信息
#         如果需要迁移项目 可以通过这个文档进行还原
#         
#     --- 他会先去这个项目对应的虚拟环境
#         如果没有 他会帮你自动创建虚拟环境
#         然后 安装 一条龙 自动化生成
#        
#  5.0 --- 查看包信息 
#          用pip list 只能查看包 不能查看包的依赖
#          用pipenv graph 
#          
#  #  6.0 --- 卸载包
#           pipenv unintall xxx
#           并且自动跟新 pipfile 和 pipfile.lock
#           这两个文件
#           
#           pipenv clean
#            卸载所有包
#       
#  7.0 --- 退出项目对应的虚拟环境
#           exit
# 8.0 --- 删除项目对应的虚拟环境
#           首先进入到项目的路径下
#           然后执行 
#           pipenv --rm
#           删除项目对应的虚拟环境   
# 
# 9.0 --- 生成requeirments.txt
#           pipenv lock -r --dev > requirements.txt
# 
# 10.0 --- 安装requeirments.txt
#           pipenv install -r requiremnet.txt
#               
# ------ 转移项目
# 
#         用pipenv创建的项目 非常好迁移
#         我们只需要拿到 整个项目文件
#         然后 进入到 这个项目文件夹下面
#         通过 pipenv install 
#         他会自动检测 pipfile 和 pipfile.lock 
#         这两个文件
#         并且安装 这连个文件中 需要的三方包 和 三方包的依赖包
#         然后自动创建出 这个项目对应的 虚拟环境
#         真是完美
#         
#         
#     创建项目虚拟环境
#     --- pipenv --python 3.7
#       
#     查看项目位置
#     --- pipevn --where
#     
#     查看虚拟环境
#     --- pipenv --venv
#  
#  root@localhost: wedJWQSkM6*-
#     
#      
# 
# Usage: pipenv [OPTIONS] COMMAND [ARGS]...

# Options:
#   --where             Output project home information.
#   --venv              Output virtualenv information.
#   --py                Output Python interpreter information.
#   --envs              Output Environment Variable options.
#   --rm                Remove the virtualenv.
#   --bare              Minimal output.
#   --completion        Output completion (to be eval'd).
#   --man               Display manpage.
#   --support           Output diagnostic information for use in GitHub
#                       issues.
#   --site-packages     Enable site-packages for the virtualenv.
#   --python TEXT       Specify which version of Python virtualenv should
#                       use.
#   --three / --two     Use Python 3/2 when creating virtualenv.
#   --clear             Clears caches (pipenv, pip, and pip-tools).
#   -v, --verbose       Verbose mode.
#   --pypi-mirror TEXT  Specify a PyPI mirror.
#   --version           Show the version and exit.
#   -h, --help          Show this message and exit.


# Usage Examples:
#    Create a new project using Python 3.7, specifically:
#    $ pipenv --python 3.7

#    Remove project virtualenv (inferred from current directory):
#    $ pipenv --rm

#    Install all dependencies for a project (including dev):
#    $ pipenv install --dev

#    Create a lockfile containing pre-releases:
#    $ pipenv lock --pre

#    Show a graph of your installed dependencies:
#    $ pipenv graph

#    Check your installed dependencies for security vulnerabilities:
#    $ pipenv check

#    Install a local setup.py into your virtual environment/Pipfile:
#    $ pipenv install -e .

#    Use a lower-level pip command:
#    $ pipenv run pip freeze

# Commands:
#   check      Checks for security vulnerabilities and against PEP 508
#              markers provided in Pipfile.
#   clean      Uninstalls all packages not specified in Pipfile.lock.
#   graph      Displays currently-installed dependency graph information.
#   install    Installs provided packages and adds them to Pipfile, or (if
#              no packages are given), installs all packages from Pipfile.
#   lock       Generates Pipfile.lock.
#   open       View a given module in your editor.
#   run        Spawns a command installed into the virtualenv.
#   shell      Spawns a shell within the virtualenv.
#   sync       Installs all packages specified in Pipfile.lock.
#   uninstall  Un-installs a provided package and removes it from Pipfile.
#   update     Runs lock, then sync.
#   
#
#
#
#
#
#
#
#
################################ pipenv 高级用法
#
# 1.0 把项目环境安装到项目里面
#       如果创建项目的时候会把虚拟环境安装到用户目录里面
#       我们预先在项目文件夹下创建.venv文件夹，当我们创建项目
#       的时候会自动把虚拟环境安装到.venv文件夹下方便管理
# 
