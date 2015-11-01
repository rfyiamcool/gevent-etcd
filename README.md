## 项目名

gevent-etcd

## 介绍

gevent-etcd 是一个使用gevent requests封装的python client模块. 至于gevent_etcd用途是用来解决在多任务请求下io阻塞的情况 (`主要是针对应用环境用gevent调度的情况下`) . etcd原版是用urllib2开发的, 我个人曾经被gevent urllib2坑过, 所以轻易不会用urllib2.  

另外，gevent-etcd的功能还很简单，期待有人提交pull request

我个人的看法，在网络io堵塞的问题上，能用协程坚决不用多线程.

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

