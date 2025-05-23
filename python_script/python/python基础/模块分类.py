'''
1、系统内置模块
　　os模块：os模块包含普遍的操作系统功能
　　sys模块：提供了一系列有关Python运行环境的变量和函数
　　random模块：random模块用于生成随机数
　　time 模块: 主要包含各种提供日期、时间功能的类和函数
　　datetime模块：对time模块的一个高级封装
　　shutil模块：是一种高层次的文件操作工具
　　logging模块：将日志打印到了标准输出中
　　re模块：可以直接调用来实现正则匹配
　　pymysql模块：连接数据库,并实现简单的增删改查
　　threading模块：提供了更强大的多线程管理方案
　　queue模块：实现了多生产者,多消费者的队列
　　json模块：用于字符串和数据类型间进行转换json
2、开源(三方)模块
　　Requests：最富盛名的http库。每个Python程序员都应该有它。
　　Scrapy：从事爬虫相关的工作，这个库也是必不可少的。
　　NumPy：为Python提供了很多高级的数学方法。
　　matplotlib：一个绘制数据图的库。对于数据分析师非常有用。
　　Pygame：开发2D游戏的时候可以用上 。
　　Scapy：用Python写的数据包探测和分析库。
　　Django：开源Web开发框架，它鼓励快速开发,并遵循MVC设计，开发周期短。
　　Py2exe：将python脚本转换为windows上可以独立运行的可执行程序。
　　BeautifulSoup：基于Python的HTML/XML解析器，简单易用。
　　PyGtk：基于Python的GUI程序开发GTK+库。
3、自定义模块
　　自定义模块是自己写的模块，对某段逻辑或某些函数进行封装后供其他函数调用。
　　注意：自定义模块的命名一定不能和系统内置的模块重名了，否则将不能再导入系统的内置模块了。
　　例如：自定义了一个sys.py模块后，再想使用系统的sys模块是不能使用的。
'''
print(__doc__)
print(dir())
print(__file__)
print(__name__)
print(__builtins__)
print(__package__)

