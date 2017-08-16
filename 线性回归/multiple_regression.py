#!/usr/bin/python
# -*- coding:utf-8 -*-

from sklearn.linear_model import LinearRegression

x=[[155,80],[157,82],[166,85],[177,90],[187,97]]
y=[[55],[60],[63],[70],[79]]
model=LinearRegression()
model.fit(x,y)

x_test=[[156,80],[163,83],[166,84],[170,87],[188,99]]
y_test=[[56],[63],[63],[72],[80]]
preditions=model.predict(x_test)
for i,predition in enumerate(preditions):
	print('Predicted:%.2f,Target:%s' % (predition,y_test[i]))
print('R-squared:%.2f' % model.score(x_test,y_test))