# --- 1.0 安装pip
#         我们安装之前 可以查看一下是否已经安装了 pip list 列出所有的 三方包
#         用 easy_install pip  安装
#         
# --- 2.0 切换安装源
#         默认的安装源是国外的 速度比较慢
#         -- pip install --index--url http://pypi.douban.com/simple/ packagename
#         来指定安装源头
#         
#         -- pip install --extra-inex-url http://https://pypi.mirrors.ustc.edu.cn/simple/
#         这中方式 是扩展 提取 也就是说 如果阿皮在pypi 里面没有检索到 就会到指定的这个库里面去检索
#         
#         -- 永久的改变安装源头
#            如果 我们不想每次都改变安装源 我们可以永久性的改变
#            1.0 先把pip升级到最新版本
#                pip install pip -U
#            2.0 设置永久的配置目录,他会自动在C:\Users\17983\AppData\Roaming\pip\pip.ini 目录下创建配置文件
#                pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
#               
# --- 3.0 查看包
#       1.0查看所有安装的包
#          pip list
#       2.0 查看不被依赖的包
#          pip list --not-required 包
#       3.0 查看过期的包
#          pip list outdated
#       4.0 查看某个包的具体信息
#        
# 
# 
# --- 4.0安装在不同版本的 python中
#      python3 -m install *****
#      python2 -m insatll *****
#      --- 安装特定版本的包
#      可以用比较符号 来指定版本的范围 用引号包起来 
#      pip instal "requests < 2" 
#      
#      --- 安装指定文件的包
#      pip install -r 文件
#      
# --- 5.0 搜索包
#       pip search 
# 
# --- 6.0 升级包
#       
#       pip install --upgrade xxx 
#       也会把他关联的包升级到 他关联的对应版本
#       
#--- 7.0 生成冻结需求的文本 
#        把所有的三方包路径 写入到文件中
#        也可以根据这个文件安装 所有的包
#          
#       ---新版ubuntu要求使用https源，要注意。

        # 清华：https://pypi.tuna.tsinghua.edu.cn/simple

        # 阿里云：http://mirrors.aliyun.com/pypi/simple/

        # 中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/

        # 华中理工大学：http://pypi.hustunique.com/

        # 山东理工大学：http://pypi.sdutlinux.org/ 

        # 豆瓣：http://pypi.douban.com/simple/

        # 临时使用：
        # 可以在使用pip的时候加参数-i https://pypi.tuna.tsinghua.edu.cn/simple

        # 例如：pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyspider，
        # 这样就会从清华这边的镜像去安装pyspider库。
    

# --- Commands:
#   install                     安装包
#   download                    下载包
#   uninstall                   卸载包
#   freeze                      输出按要求格式安装的软件包
#   list                        查看已经安装的包
#   show                        显示有关已安装包的信息
#   check                       验证已安装的包具有兼容的依赖关系
#   config                      管理本地和全局配置.
#   search                      搜索PyPI中的包.
#   wheel                       根据你的要求制造轮子.
#   hash                        计算软件包档案的散列.
#   completion                  用于命令完成的助手命令。
#   help                        用于命令完成的助手命令。

# General Options:
#   -h, --help                  显示帮助.
#   --isolated                  以隔离模式运行pip，忽略环境变量和用户配置。
#   -v, --verbose               提供更多的产出。选项是附加的，最多可使用3次
#   -V, --version               显示版本并退出
#   -q, --quiet                 给更少的输出。选项是可添加的，最多可使用3次(对应于警告、错误和关键日志级别).
#   --log <path>                一个详细的附加日志的路径.
#   --proxy <proxy>             在[user:passwd@]proxy.server:port中指定代理。
#   --retries <retries>         每个连接应该尝试的最大重试次数(默认为5次)。
#   --timeout <sec>             设置套接字超时(默认为15秒).
#   --exists-action <action>    当路径已经存在时的默认操作:(s)witch， (i)gnore， (w)ipe， (b)ackup， (a)bort)。
#   --trusted-host <hostname>   将此主机标记为受信任的，即使它没有有效或任何HTTPS。
#   --cert <path>               替换CA包的路径.
#   --client-cert <path>        SSL客户端证书的路径，一个包含私钥和PEM格式证书的文件.
#   --cache-dir <dir>           存储缓存数据在 <dir>.
#   --no-cache-dir              禁用缓存.
#   --disable-pip-version-check
#                               不要定期检查PyPI以确定是否有新的pip版本可供下载。暗示,没有索引.
#   --no-color                  抑制彩色输出
#   
#   ############################################ 安装 install ###############################
#   用法:
#   pip install [options] <要求说明符> [package-index-options] ...
#   pip install [options] -r <需求文件> [package-index-options] ...
#   pip install [options] [-e] <风险投资项目的url> ...
#   pip install [options] [-e] <当地项目路径> ...
#   pip install [options] <归档文件的url /路径> ...

# 描述:
#   安装包的:

#   - 使用需求说明符的PyPI(和其他索引).
#   - VCS工程的url.
#   - 本地项目目录.
#   - 本地或远程源存档.

#   pip还支持从提供的“需求文件”安装
#  指定要安装的整个环境的一种简单方法.

# 安装选项:
#   -r, --requirement <file>    从给定的需求文件安装。这个选项可以多次使用。
#   -c, --constraint <file>     使用给定的约束文件约束版本。这个选项可以多次使用.
#   --no-deps                   不要安装包依赖项。
#   --pre                       包括预发布和开发版本。默认情况下，pip只找到稳定的版本.
#   -e, --editable <path/url>   从本地项目路径或VCS url以可编辑模式(即setuptools“开发模式”)安装项目.
#   -t, --target <dir>          将包安装到
                                # 。默认情况下，这不会替换
                                # 中的现有文件/文件夹。使用—升级以用new替换
                                # 中的现有包
                                # #版本.
#   --platform <platform>       Only use wheels compatible with <platform>. Defaults to the platform of the running system.
#   --python-version <python_version>
#                               Only use wheels compatible with Python interpreter version <version>. If not specified, then the current system interpreter minor version is used. A major
#                               version (e.g. '2') can be specified to match all minor revs of that major version.  A minor version (e.g. '34') can also be specified.
#   --implementation <implementation>
#                               Only use wheels compatible with Python implementation <implementation>, e.g. 'pp', 'jy', 'cp',  or 'ip'. If not specified, then the current interpreter
#                               implementation is used.  Use 'py' to force implementation-agnostic wheels.
#   --abi <abi>                 Only use wheels compatible with Python abi <abi>, e.g. 'pypy_41'.  If not specified, then the current interpreter abi tag is used.  Generally you will need
#                               to specify --implementation, --platform, and --python-version when using this option.
#   --user                      Install to the Python user install directory for your platform. Typically ~/.local/, or %APPDATA%\Python on Windows. (See the Python documentation for
#                               site.USER_BASE for full details.)
#   --root <dir>                Install everything relative to this alternate root directory.
#   --prefix <dir>              Installation prefix where lib, bin and other top-level folders are placed
#   -b, --build <dir>           Directory to unpack packages into and build in. Note that an initial build still takes place in a temporary directory. The location of temporary directories
#                               can be controlled by setting the TMPDIR environment variable (TEMP on Windows) appropriately. When passed, build directories are not cleaned in case of
#                               failures.
#   --src <dir>                 Directory to check out editable projects into. The default in a virtualenv is "<venv path>/src". The default for global installs is "<current dir>/src".
#   -U, --upgrade               Upgrade all specified packages to the newest available version. The handling of dependencies depends on the upgrade-strategy used.
#   --upgrade-strategy <upgrade_strategy>
#                               Determines how dependency upgrading should be handled [default: only-if-needed]. "eager" - dependencies are upgraded regardless of whether the currently
#                               installed version satisfies the requirements of the upgraded package(s). "only-if-needed" -  are upgraded only when they do not satisfy the requirements of
#                               the upgraded package(s).
#   --force-reinstall           Reinstall all packages even if they are already up-to-date.
#   -I, --ignore-installed      Ignore the installed packages (reinstalling instead).
#   --ignore-requires-python    Ignore the Requires-Python information.
#   --no-build-isolation        Disable isolation when building a modern source distribution. Build dependencies specified by PEP 518 must be already installed if this option is used.
#   --install-option <options>  Extra arguments to be supplied to the setup.py install command (use like --install-option="--install-scripts=/usr/local/bin"). Use multiple --install-option
#                               options to pass multiple options to setup.py install. If you are using an option with a directory path, be sure to use absolute path.
#   --global-option <options>   Extra global options to be supplied to the setup.py call before the install command.
#   --compile                   Compile Python source files to bytecode
#   --no-compile                Do not compile Python source files to bytecode
#   --no-warn-script-location   Do not warn when installing scripts outside PATH
#   --no-warn-conflicts         Do not warn about broken dependencies
#   --no-binary <format_control>
#                               Do not use binary packages. Can be supplied multiple times, and each time adds to the existing value. Accepts either :all: to disable all binary packages,
#                               :none: to empty the set, or one or more package names with commas between them. Note that some packages are tricky to compile and may fail to install when
#                               this option is used on them.
#   --only-binary <format_control>
#                               Do not use source packages. Can be supplied multiple times, and each time adds to the existing value. Accepts either :all: to disable all source packages,
#                               :none: to empty the set, or one or more package names with commas between them. Packages without binary distributions will fail to install when this option
#                               is used on them.
#   --prefer-binary             Prefer older binary packages over newer source packages.
#   --no-clean                  Don't clean up build directories.
#   --require-hashes            Require a hash to check each requirement against, for repeatable installs. This option is implied when any package in a requirements file has a --hash
#                               option.
#   --progress-bar <progress_bar>
#                               Specify type of progress to be displayed [off|on|ascii|pretty|emoji] (default: on)

# Package Index Options:
#   -i, --index-url <url>       Python包索引的基本URL(默认https://pypi.org/simple)。这应该指向符合PEP 503(简单的存储库API)或a的存储库
#                               local directory laid out in the same format.
#   --extra-index-url <url>     Extra URLs of package indexes to use in addition to --index-url. Should follow the same rules as --index-url.
#   --no-index                  Ignore package index (only looking at --find-links URLs instead).
#   -f, --find-links <url>      If a url or path to an html file, then parse for links to archives. If a local path or file:// url that's a directory, then look for archives in the
#                               directory listing.
#   --process-dependency-links  Enable the processing of dependency links.