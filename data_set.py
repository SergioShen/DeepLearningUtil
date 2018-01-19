#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 6:29 2018/1/19
# @Author: Shen Sijie
# @File: data_set
# @Project: DeepLearningTemplates


from abc import abstractmethod
import random


class BasicDataSet(object):
    """
    Basic data set class, contains *next_batch* and *random_batch* method
    """

    def __init__(self):
        """
        Set *pointer* to zero
        """
        self.pointer = 0

    @abstractmethod
    def size(self):
        """
        Get size of the data set, sub class must implement this method
        :return: size of the data set
        """
        pass

    @abstractmethod
    def __getitem__(self, index):
        """
        Get a piece of data with index, sub class must implement this method
        :param index: index of the data
        :return: content of data
        """
        pass

    @abstractmethod
    def shuffle(self):
        """
        Shuffle the data set, sub class must implement this method
        :return: None
        """
        pass

    def next_batch(self, batch_size):
        """
        Get next batch of data set
        :param batch_size: batch size
        :return: next batch data of *data_size*, won't repeat within a epoch
        """
        if batch_size > self.size():
            # Raise an error if request batch size is greater than the size of data set
            raise IndexError

        if self.pointer + batch_size > self.size():
            # An epoch passed, shuffle and reset the current point
            self.shuffle()
            self.pointer = 0

        return [self[i] for i in range(self.pointer, self.pointer + batch_size)]

    def random_batch(self, batch_size=None):
        """
        Get a random batch of data set
        :param batch_size: batch size
        :return: a batch data of *data_size*
        """
        if batch_size is None:
            samples = range(self.size())
        else:
            if batch_size > self.size():
                # Raise an error if request batch size is greater than the size of data set
                raise IndexError
            samples = random.sample(range(self.size()), batch_size)

        return [self[i] for i in samples]
