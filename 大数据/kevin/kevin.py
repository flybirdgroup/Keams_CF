# -*- coding=utf-8 -*-
import pandas as pd
import numpy as np
import scipy.optimize as sco
import matplotlib.pyplot as plt

prices=pd.read_excel('./上证50成分股.xlsx',header=0,index_col=0)
returns=np.log(prices/prices.shift(1))
returns=returns.dropna()
returns_15to17=returns.loc['2015-01-01':'2017-12-31']
returns_mean=returns_15to17.mean()*252
print('股票 2015 年至 2017 年的年化平均收益率\n',returns_mean.round(6))
vol=returns_15to17.std()*np.sqrt(252)
returns_cov=returns_15to17.cov()*np.sqrt(252)
def F(w):
    Rf=0.0169428
    w=np.array(w)
    Rp=np.sum(w*returns_mean)
    Vp=np.sqrt(np.dot(w,np.dot(returns_cov,w.T)))
    SR=(Rp-Rf)/Vp
    return np.array([Rp,Vp,SR])
def SRmin_F(w):
    return -F(w)[2]

cons=({'type':'eq','fun':lambda x: np.sum(x)-1})
bnds=tuple((0,1) for x in range(len(returns_mean)))
w0=np.ones_like(returns_mean)/len(returns_mean)
result=sco.minimize(SRmin_F,w0,method='SLSQP',bounds=bnds,constraints=cons)

weight=result['x']
stock_name=returns_mean.index

for i in range(len(returns_mean)):
    print(stock_name[i],round(weight[i],6))

Index_18to19=pd.read_excel('./2018年至2019年9月道琼斯工业平均指数的日收盘价.xlsx',sheet_name="Sheet1",header=0,index_col=0)
Index_18to19=100*(Index_18to19/Index_18to19.iloc[0])
prices_18to19=prices.loc['2018-01-01':'2019-09-30']
port_price_18to19=100*np.sum(weight*prices_18to19/prices_18to19.iloc[0],axis=1)
plt.figure(figsize=(9,6))
plt.plot(port_price_18to19,'r-',label=u'按最优权重配置的投资组合',lw=2.5)
plt.plot(Index_18to19,'c-',label=u'道琼斯工业平均指数',lw=2.5)
plt.xlabel(u'日期',fontsize=13)
plt.xticks(fontsize=13,rotation=20)
plt.ylabel(u'价格',fontsize=13)
plt.yticks(fontsize=13)
plt.title(u'按照最优权重配置的投资组合与道琼斯工业平均指数的日走势', fontsize=14)
plt.legend(fontsize=13)
plt.grid('True')
plt.show()