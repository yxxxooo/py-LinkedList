#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from item import Items


class ArrayList(object):

    def __init__(self):
        self.length = 0
        self.items = None
        self._head_item = None
        self._bottom_item = None

    def iteration(self, iteration_item, index):
        if iteration_item.item_index == index or index <= 0:
            return iteration_item
        else:
            return self.iteration(iteration_item.item_next, index)

    def get(self, index):
        if index < 0 or self.length < index:
            return False
        return self.iteration(self._head_item, index).item_obj

    def add(self, item_obj, index=-1):
        items = Items()
        items.item_obj = item_obj
        items.item_index = index

        if self._head_item is None:
            self._head_item = items
        if self._bottom_item is None:
            self._bottom_item = items

        if index <= -1 or index >= self.length:
            items.item_index = self.length
            items.item_next = None
            self._bottom_item.item_next = items
            self._bottom_item = items
            self.length += 1
            return

        for key in reversed(range(index, self.length)):
            update_item = self.iteration(self._head_item, key)
            update_item.item_index += 1

        if index == 0:
            items.item_next = self._head_item
            self._head_item = items
        else:
            last_item = self.iteration(self._head_item, index-1)
            items.item_next = last_item.item_next
            last_item.item_next = items

        self.length += 1

    def get_all(self):
        return_list = []
        for key in range(self.length):
            return_list.append(self.iteration(self._head_item, key).item_obj.__dict__)
        return return_list

    def remove(self, index):
        if self.length < index or index < 0:
            return False

        next_item = self.iteration(self._head_item, index + 1)
        if index == 0:
            self._head_item = next_item
        else:
            last_item = self.iteration(self._head_item, index - 1)
            last_item.item_next = next_item

        for key in reversed(range(index+1, self.length)):
            update_item = self.iteration(self._head_item, key)
            update_item.item_index -= 1

        self.length -= 1

    def update(self, index, item_obj):
        if self.length < index or index < 0:
            return False

        item = self.iteration(self._head_item, index)
        item.item_obj = item_obj
        return item
