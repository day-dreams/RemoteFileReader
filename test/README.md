这个目录下是在学习grpc和protobuf过程中留下的小demo。


调用protoc生成代码的命令如下:
```bash
python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. Echo.proto 
```

总体流程就是:

* client  
grpc.channel+stub+request

* server  
grpc.server+Servicer