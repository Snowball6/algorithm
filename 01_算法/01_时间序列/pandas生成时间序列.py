#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time   : 2020/6/8 16:28
# @Author : Snowball

import pandas as pd
import numpy as np

# 时间序列
# 时间戳（timestamp）
# 固定周期（period）
# 时间间隔（interval）

# date_range
# 可以指定开始时间与周期
# H：小时
# D：天
# M：月

# TIMES #2016 Jul 1 7/1/2016 1/7/2016 2016-07-01 2016/07/01
rng = pd.date_range('2016-07-01', periods = 10, freq = '3D')
rng

time=pd.Series(np.random.randn(20),
           index=pd.date_range(dt.datetime(2016,1,1),periods=20))
print(time)

# truncate过滤
time.truncate(before='2016-1-10')
time.truncate(after='2016-1-10')
print(time['2016-01-15'])
print(time['2016-01-15':'2016-01-20'])
data=pd.date_range('2010-01-01','2011-01-01',freq='M')
print(data)

#时间戳
pd.Timestamp('2016-07-10')