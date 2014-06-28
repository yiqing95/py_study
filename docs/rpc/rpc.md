RPC
====

rpc 允许你像调用本地库那样的使用方式来调用远程的方法 以下两种情形常可以考虑使用之：
-  功能分解，一个功能需要做很多事情 可以把这些子功能让多个不同的机器来处理。主动使用！
-  合并收集信息，所需要的信息位于不同位置，rpc可以帮我们取回这些信息。 有点被动！

最早的远程过程调用多是c语言实现，协议常识面向字节的，字节流发送，如：
0, 0, 0, 1, 64, 36, 0, 0, 0, 0, 0, 0

再往后出现了xml发送的参数：
<params>
<param><value><i4>41</i4></value></param>
<param><value><double>10.</double></value></param>
</params>
现今json格式比较普遍使用了：
[1, 10.0]

## RPC特征：
当你部署rpc客户端或者服务器时你需要知道rpc的优缺点。
- rpc机制都有其限制，rpc一般倾向跨语言调用，参数类型有限，劲量使用多种语言的基本类型的交集
- 有些资源性的变量不可以使用，无法通过网络传输：如文件句柄，套接字，共享内存..
- 错误异常的处理，server端毕竟不和client端在一个地址空间 如果server调用出错了，异常栈信息对
    client端是没有意义的！这时可以通过异常转换，传递错误消息等手段。【其实golang的ok comma模式
    就很不错哦！】发生在server端的异常 在client端是不是同样要表现出是异常！
- 许多rpc实现都提供自举功能，可以列举自举提供了那些api 参数及其返回值等信息！python是弱类型语言
    所以在这方面可能弱些 不及强类型语言。
- 有些复杂的实现会支持访问控制，大部分的实现没有这些东西，验证可能会基于底层的如http协议

## xmlRpc ：
------------------
Purpose: Remote procedure calls
Standard: www.xmlrpc.com/spec
Runs atop: HTTP
Data types: int; float; unicode; list; dict with unicode keys; with non-standard extensions, datetime
and None
Libraries: xmlrpclib, SimpleXMLRPCServer, DocXMLRPCServer

## jsonRpc
-----------------
Purpose: Remote procedure calls
Standard: http://json-rpc.org/wiki/specification
Runs atop: HTTP
Data types: int; float; unicode; list; dict with unicode keys; None
Libraries: many third-party, including lovely.jsonrpc
