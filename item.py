#!/usr/bin/env python 
# -*- coding:utf-8 -*-


class Items(object):

    def __init__(self, index=0, item_obj=None):
        self.item_index = index
        self.item_obj = item_obj
        self.item_next = None
