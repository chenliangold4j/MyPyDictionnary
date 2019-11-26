print("test")
# 1．选择新建一个Pure Python项目，新建项目路径可以在Location处选择。
#
# 2.Project Interpreter部分是选择新建项目所依赖的python库，第一个选项会在项目中简历一个venv（virtualenv）目录，这里存放一个虚拟的python环境。这里所有的类库依赖都可以直接脱离系统安装的python独立运行。
#
# 3.Existing Interpreter关联已经存在的python解释器，如果不想在项目中出现venv这个虚拟解释器就可以选择本地安装的python环境。
#
# 那么到底这两个该怎么去选择呢，这里建议选择New Environment 可以在Base Interpreter选择系统中安装的Python解释器，这样做的好处有很多。
#
# python项目可以独立部署
# 防止一台服务器部署多个项目之间存在类库的版本依赖问题发生
# 也可以充分发挥项目的灵活性