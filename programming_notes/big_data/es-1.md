# Elasticsearch系列(一)

> 环境：CentOS 7.5 + Elasticsearch 6.3.2 + Logstash 6.3.2

## 介绍

> Elasticsearch是一个基于Lucene的搜索和数据分析工具，它提供了一个分布式服务。
>
> Elasticsearch是遵从Apache开源条款的一款开源产品，是当前主流的企业级搜索引擎。

## 版本

* 常用版本是5.3和6.3
* 官方最新稳定版是6.6
* 6.3之后的版本支持SQL方式查询数据

## 安装

1. 从[ES官网](https://www.elastic.co/)下载二进制压缩包、解压
2. 配置环境变量

```bash
# 下面是ES安装命令，前提是已经配置JAVA环境
cd /usr/local/src
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.3.2.tar.gz
tar zxf elasticsearch-6.3.2.tar.gz -C /usr/local/
export ES_HOME=/usr/local/elasticsearch
export PATH=$PATH:$ES_HOME/bin
```

## 启动

```bash
# 启动ES
elasticsearch

# 查看当前节点信息
curl localhost:9200
{
  "name" : "Ion8fvz",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "olyx-NO6Sq6d9Uu6XlQ03w",
  "version" : {
    "number" : "6.3.2",
    "build_flavor" : "default",
    "build_type" : "tar",
    "build_hash" : "053779d",
    "build_date" : "2018-07-20T05:20:23.451332Z",
    "build_snapshot" : false,
    "lucene_version" : "7.3.1",
    "minimum_wire_compatibility_version" : "5.6.0",
    "minimum_index_compatibility_version" : "5.0.0"
  },
  "tagline" : "You Know, for Search"
}
```

* ES进程默认通讯端口是 `9200`
* 守护进程方式的启动命令是 `elasticsearch -d`

