os模块
============
乾坤 阴阳是起源。

os模块是最大的两个模块之一（另一个是sys模块），类似太极图中的黑或者白。
其囊括常见在c语言中的脚本调用，shell编程所用到的os操作，如目录，进程，shell变量等。
从技术角度讲它提供了POSIX工具能力（可移植操作系统调用接口），加上平台无关的目录处理能力os.path模块
操作角度讲os模块提平台供了大量的对底层操作系统的接口，可以做到一处编写多处运行！
在某些平台，他也提供了平台特定的功能封装。

常用功能
-----------

~~~
Shell variables os.environ
Running programs os.system, os.popen, os.execv, os.spawnv
Spawning processes os.fork, os.pipe, os.waitpid, os.kill
Descriptor files, locks os.open, os.read, os.write
File processing os.remove, os.rename, os.mkfifo, os.mkdir, os.rmdir
Administrative tools os.getcwd, os.chdir, os.chmod, os.getpid, os.listdir, os.access
Portability tools os.sep, os.pathsep, os.curdir, os.path.split, os.path.join
Pathname tools os.path.exists('path'), os.path.isdir('path'), os.path.getsize('path')
~~~
