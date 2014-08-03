从 0  写django 测试程序

从哪里开始
--------------
    所有的.py 结尾的文件直接可以当脚本运行。这是因为文件关联的原因。如果没有关联 需要前面
    加上python 如： python xxx.py .....

-  先写个功能测试  使用selenium
-  创建django项目：
    ~~~
        django-admin.py startproject superlists
    ~~~
    竟然可以直接运行 不知道咋找到那个脚本的！

-  运行web项目：
    ~~~
        manage.py runserver
    ~~~
-   运行我们的测试脚本：
    ~~~
        functional_tests.py
    ~~~
    如果没有出现任何错误 那么测试成功了！！！

-  添加db文件到 gitignore：
    ~~~
        echo db.sqlite3 >> .gitignore
    ~~~

-  使用unittest 来做功能测试的框架
    为我们的测试命名 设计类、方法。

构建我们的app
---------------

-  django 推荐一个web项目由若干个app构成
-  使用命令来添加一个新的app：
   ~~~
   manage.py startapp lists
   ~~~

-  app目录中有django自带的test框架实现！！！
   修改
-  运行django的测试：
    ~~~
    manage.py test
    ~~~
    这个命令会运行所有的测试的包括django自带的一些测试

    通过指定参数 可以缩小测试范围：
    ~~~
    manage.py test lists
    ~~~
    指定的lists是app名字 但这个app要添加到项目的安装app列表中：
    ~~~

        INSTALLED_APPS = (
            'lists',

            'django.contrib.auth',
            'django.contrib.contenttypes',
            ...ss
        )

    ~~~

    然后再次运行测试！！！

##  测试驱动的流程
    测试驱动的web开发是一个循环开发测试代码---》 回到app开发使测试通过
        再回到写测试代码，再次使得测试通过的循环过程

        测试总是先行于app代码编写。