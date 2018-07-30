'''
Created on Jul 30, 2018

@author: kaka
'''
from pandas import read_csv
from pandas import set_option
filename = 'abalone.csv'
names = ['Sex','Length','Diameter','Height','Whole weight','Shucked weight',
         'Viscera weight','Shell weight','Rings']
data = read_csv(filename, names=names)
set_option('display.width', 120)
set_option('precision', 4)
print(data.shape)
# print(data.head(10))
print(data.dtypes)   ####数据类型
print(data.describe()) ####数据描述
print(data.groupby('Rings').size())   ####分类统计
print(data.corr(method='pearson'))    ####变量相关性
print(data.skew())




