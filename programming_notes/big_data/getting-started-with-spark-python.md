# Spark 快速入门 - Python 语言

原文： <http://spark.apache.org/docs/latest/quick-start.html>

译文： <https://luoxu34.github.io/2018/06/09/spark-快速入门---python-语言/>

译者： [luoxu34](https://github.com/luoxu34)

时间： 2018/06/09

环境:

| Name    | Version          |
| ------- | ---------------- |
| OS      | Ubuntu 18.04 LTS |
| JDK     | 8u172            |
| Python  | 3.6.5            |
| PySpark | 2.3.0            |

------

> 需要了解的是，Spark 2.0 之前的版本，主要的编程接口是弹性分布式数据集(Resilient Distributed Dataset, 简称**RDD**)。在 Spark 2.0 之后的版本虽然依旧支持 RDD，但是 RDD 已经被数据集 **Dataset** 所取代，后者不但是强类型的，而且与 RDD 相比具有更多的改进和优化，因此强烈建议使用 Dataset 而不是 RDD。

# 使用Spark Shell进行交互式分析

## 基础 Basics

Spark shell提供了一种学习API的简单方法，它同时也是交互式分析数据的强大工具。 第一步，需要进入 Spark 的交互模式：

```
$ pyspark
```

Spark 的主要抽象是一个称为数据集的分布式项目集合。数据集可以通过 Hadoop 的 InputFormats（例如 HDFS 文件）创建，或通过其他数据集转换而来。由于 Python 的动态特性，我们不要求在 Python 中数据集是强类型。因此，Python 中的所有数据集都是 `Dataset[Row]`，我们称之为 `DataFrame`，这与 Pandas 和 R 中的数据框架概念一致。

让我们利用 Spark 源目录中的 README 文件来创建一个新 DataFrame 对象：

```
>>> textFile = spark.read.text("README.md")
```

我们可以调用转换函数获得一个新的 DataFrame 对象，或者调用动作函数计算得到返回值。

如果想要了解更多内容，请移步阅读相关的[API文档](http://spark.apache.org/docs/latest/api/python/index.html#pyspark.sql.DataFrame)。

```
>>> textFile.count()  # Number of rows in this DataFrame
126

>>> textFile.first()  # First row in this DataFrame
Row(value=u'# Apache Spark')
```

现在让我们将这个 DataFrame 转换成一个新的。通过调用 filter 函数来返回一个包含 Spark 字符串行的新 DataFrame 对象。

```
>>> linesWithSpark = textFile.filter(textFile.value.contains("Spark"))
```

当然，我们也可以把转换和动作串连起来一并执行：

```
>>> textFile.filter(textFile.value.contains("Spark")).count()
15
```

## 更多的数据集操作

数据集 Dataset 动作(**actions**)和转换(**transformations**)可用于更复杂的计算。例如我们想要获得最多单词的行号，可以这样：

```
>>> from pyspark.sql.functions import *
>>> textFile.select(size(split(textFile.value, "\s+")).name("numWords")).agg(max(col("numWords"))).collect()
[Row(max(numWords)=15)]
```

首先是map过程：统计每一行的单词数并命名为 “numWords”，得到一个新的 DataFrame 对象。最后是reduce过程：调用 DataFrame 对象的 agg 方法找到最大的 numWords 值。

`select` 函数和 `agg` 函数的参数都是列 Column，我们可以通过 `df.colName` 方式得到 DataFarme 的列。我们也可以导入 pyspark.sql.functions 模块，它提供了很多方便的功能从旧 Column 对象构建一个新的对象。

Spark 可以轻松地实现 Hadoop 的 MapReduce 数据流模式：

```
>>> wordCounts = textFile.select(explode(split(textFile.value, "\s+")).alias("word")).groupBy("word").count()
```

为了得到最后的结果，我们需要调用 collect 函数执行计算：

```
>>> wordCounts.collect()
[Row(word=u'online', count=1), Row(word=u'graphs', count=1), ...]
```

## 缓存 Caching

Spark 也支持将数据集存入集群范围的内存缓存中。这对于需要进行重复访问的数据非常有用，比如我们需要在一个小的数据集中执行查询操作，或者需要执行一个迭代算法（例如PageRank）。 一个简单的例子，我们可以把 `linesWithSpark` 数据集进行缓存，就像这样：

```
>>> linesWithSpark.cache()
>>> linesWithSpark.count()
15
>>> linesWithSpark.count()
15
```

使用 Spark 去处理和缓存100行的文本似乎没有什么意义。但实际的情景是，你可以使用这些函数去操作非常大的数据集，即使它们被分布在成百上千的节点上。

你也可以通过 bin/pyspark 连接到集群中以交互方式执行此操作，详情请见[RDD编程指南](http://spark.apache.org/docs/latest/rdd-programming-guide.html#using-the-shell)。

# 自包含的应用程序

现在我们将展示如何使用 Python API（PySpark）编写应用程序。

作为一个例子，我们可以创建一个简单的 Spark 应用程序，`SimpleApp.py`：

```
"""SimpleApp.py"""
from pyspark.sql import SparkSession

logFile = "YOUR_SPARK_HOME/README.md"  # Should be some file on your system
spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
logData = spark.read.text(logFile).cache()

numAs = logData.filter(logData.value.contains('a')).count()
numBs = logData.filter(logData.value.contains('b')).count()

print("Lines with a: %i, lines with b: %i" % (numAs, numBs))

spark.stop()
```

运行程序：

```
# Use the Python interpreter to run your application
$ python SimpleApp.py
...
Lines with a: 46, Lines with b: 23
```

# 更多

- 为了深入了解Spark的API，你需要阅读[RDD编程](http://spark.apache.org/docs/latest/rdd-programming-guide.html)和[SQL编程](http://spark.apache.org/docs/latest/rdd-programming-guide.html)章节。

- 如果想要在集群上运行你的程序，需要了解[部署概览](http://spark.apache.org/docs/latest/rdd-programming-guide.html)一章。

- 最后，Spark自带了几个例子在 `examples` 目录下，你可以这样去运行它们：

  ```
  # For Scala and Java, use run-example:
  ./bin/run-example SparkPi
  
  # For Python examples, use spark-submit directly:
  ./bin/spark-submit examples/src/main/python/pi.py
  
  # For R examples, use spark-submit directly:
  ./bin/spark-submit examples/src/main/r/dataframe.R
  ```

