# 一般来说，第三方库都会在Python官方的pypi.python.org网站注册，要安装一个第三方库，必须先知道该库的名称，可以在官网或者pypi上搜索，比如Pillow的名称叫Pillow，因此，安装Pillow的命令就是：
#
# pip install Pillow

# 在使用Python时，我们经常需要用到很多第三方库，例如，上面提到的Pillow，以及MySQL驱动程序，Web框架Flask，科学计算Numpy等。
# 用pip一个一个安装费时费力，还需要考虑兼容性。我们推荐直接使用Anaconda，
# 这是一个基于Python的数据处理和科学计算平台，
# 它已经内置了许多非常有用的第三方库，我们装上Anaconda，就相当于把数十个第三方模块自动安装好了，非常简单易用。
# pip 最常用命令
# 显示版本和路径
#
# pip --version
# 获取帮助
#
# pip --help
# 升级 pip
#
# pip install -U pip
# 如果这个升级命令出现问题 ，可以使用以下命令：
#
# sudo easy_install --upgrade pip
# 安装包
#
# pip install SomePackage              # 最新版本
# pip install SomePackage==1.0.4       # 指定版本
# pip install 'SomePackage>=1.0.4'     # 最小版本
# 比如我要安装 Django。用以下的一条命令就可以，方便快捷。
#
# pip install Django==1.7
# 升级包
#
# pip install --upgrade SomePackage
# 升级指定的包，通过使用==, >=, <=, >, < 来指定一个版本号。
#
# 卸载包
#
# pip uninstall SomePackage
# 搜索包
#
# pip search SomePackage
# 显示安装包信息
#
# pip show
# 查看指定包的详细信息
#
# pip show -f SomePackage
# 列出已安装的包
#
# pip list
# 查看可升级的包
#
# pip list -o