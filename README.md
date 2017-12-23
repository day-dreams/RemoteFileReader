RemoteFileReader
------------------------------------------
------------------------------------------

<!-- TOC -->

- [What is RemoteFileReader?](#what-is-remotefilereader)
- [Why RemoteFileReader?](#why-remotefilereader)

<!-- /TOC -->

# What is RemoteFileReader?

RemoteFileReader是一个基于rpc的远程文件浏览应用。

这个应用以rpc的形式提供服务，用户把文件放在远程机器上，在本地机器上运行代码来访问之。代码的访问形式就像是访问本地文件一样，只不过文件实际上在远程机器上。

在访问文件之前，用户需要做好这些工作：

* 设置好认证密码(防止文件泄漏)
* 设置好远程机器上可以访问的文件列表
* 提供待访问文件在远程机器上的路径名

总的来说，RemoteFileReader就像是一个提供极细粒度文件访问功能的简易版FTP。

# Why RemoteFileReader?

最近在分析一份数据，数据文件非常大，我的个人电脑不好直接存下来，只好放在空间足够大的服务器上。

每次分析，都需要把代码放到服务器上去分析，有点不方便。对我来说，如果能有一种能按行访问文件的rpc服务，带来的方便将远大与牺牲掉的性能。

正好最近也想学习一下流行的rpc框架，这是个很好的练习。

初步想法是使用protobuf+grpc来实现这个功能。