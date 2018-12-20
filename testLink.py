#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import json
import time

from ArrayList import ArrayList
from user import User

start = time.clock()
print("start：" + str(start))
user1 = User(1, 'yinx')
user2 = User(2, 'zhaokun')
user3 = User(3, 'yanglei')
user4 = User(4, 'lvyan')
user5 = User(5, 'liyu')
user6 = User(6, 'shanpeng')

user7_2 = User(2,'gy')

list = ArrayList()
list.add(user1)
list.add(user2)
list.add(user3)
list.add(user4)
list.add(user5)
list.add(user6)
list.add(user7_2, 0)
print(json.dumps(list.get_all()))
print(json.dumps(list.get(2).__dict__))
print(json.dumps(list.get(3).__dict__))
print(list.length)
list.remove(0)
print(json.dumps(list.get_all()))
print(list.length)
list.update(1,user7_2)
print(json.dumps(list.get_all()))
end = time.clock()
print("end：" + str(end))
print(end - start)
