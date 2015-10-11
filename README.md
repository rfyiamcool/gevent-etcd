## 项目名

gevent-etcd

## 介绍

使用gevent requests封装的一个python client模块 这模块替换了urllib http模块，采用gevent requests来访问etcd http api，用来解决在多任务下会发生io阻塞的情况。


## 用法

pypi安装
```
pip install gevent_etcd
```

源码安装

```
git clone https://github.com/rfyiamcool/gevent-etcd.git
cd gevent-etcd
python setup.py install
```

### ToDOList

1. complement write function 

2. fix stream watch bug

3. Add leader api , manage etcd cluster

