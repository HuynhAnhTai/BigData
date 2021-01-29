# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kmkn6H5lXo2t-GpioZBMZSpNvmIuneX7
"""

!pip install pyspark

import pyspark
from pyspark import SparkConf, SparkContext
import collections

conf = SparkConf().setMaster('local').setAppName('total number')
sc = SparkContext.getOrCreate(conf=conf)

def sum(x,y):
  if(x!="numbers" and y!="numbers"):
    return float(x)+float(y)
  return 0

rdd = sc.textFile("number.csv")
data = rdd.reduce(lambda x,y: sum(x,y))
print(data)