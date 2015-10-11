## 项目名

gevent-etcd

## 介绍

gevent-etcd 是一个使用gevent requests封装的python client模块. gevent-etcd用来解决在多任务并发下有io阻塞的情况. 要知道在github中有不少etcd的python模块，但是基本用都采用urllib http模块.跟gevent不怎么兼容. 虽然可以利用threading 、multiprocessing进行并发处理，但gevent协程的好处，我想大家知道！

我个人的看法，在网络io堵塞的问题上，能用协程坚决不用线程.

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

