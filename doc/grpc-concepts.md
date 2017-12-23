grpc concepts
------------------------
------------------------

[grpc concepts](https://grpc.io/docs/guides/concepts.html)

# overview

gRPC是一个基于服务(service)的rpc框架，它默认使用protocol buffers作为接口定义语言(InterfaceDefinitionLanguage)。


一共有四种service:

* Unary RPCs   
client向server发送一个请求，server返回一个响应

* Server streaming RPCs   
client向server发送一个请求，server返回一个流对象stream，client从stream中读取多个响应

* Client streaming RPCs  
client使用一个stream，向stream写入多个请求，但最终的到来自server的一个响应。

* Bidirectional streaming RPCs  
client和server都采用stream，可以发送多个请求/响应。


gRPC在大多数语言下提供了同步/异步选项。


# RPC life cycle

现在来看看不同类型服务的rpc调用期间发生了什么。

grpc有几个概念。


* Deadlines/Timeouts

* RPC termination  
在一次rpc调用中，client和server对于调用的结束结束状态有这不同的判断。举个例子，server发挥一个响应，认为这次rpc成功结束;但client却在deadlines之后才收到这个响应，会认为rpc失败.

* Cancelling RPCs  
在一次rpc调用中，client和server都可以取消这个调用,并且保证是立即取消，不在做任何工作。但是，grpc不会为这次调用提供回滚功能，也就是说，取消之前发生的事情是无法恢复的。

* Metadata  
元数据，就是关于一次rpc调用的一些信息，包括认证信息d等。

* Channels  
在某些语言里，grpc提供对于频道状态的查询功能。
