#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 5:50 2018/1/19
# @Author: Shen Sijie
# @File: vocab
# @Project: DeepLearningTemplates


import copy


class Vocabulary(object):
    def __init__(self, reserved_words=None):
        self.index_to_word = {}
        self.word_to_index = {}
        self.reserved_words = []
        self.word_to_frequency = {}

        if reserved_words is not None:
            self.reserved_words = copy.deepcopy(reserved_words)
            for item in reserved_words:
                self.add(item)

    def size(self):
        return len(self.index_to_word)

    def get_index(self, word, default=None):
        try:
            return self.word_to_index[word]
        except KeyError:
            return default

    def get_word(self, index, default=None):
        try:
            return self.index_to_word[index]
        except KeyError:
            return default

    def add(self, word):
        if word in self.word_to_index:
            self.word_to_frequency[word] += 1
            index = self.word_to_index[word]
        else:
            index = len(self.index_to_word)
            self.index_to_word[index] = word
            self.word_to_index[word] = index
            self.word_to_frequency[word] = 1
        return index

    def get_all_words(self):
        return self.word_to_index.keys()

    def delete_low_frequency_words(self, threshold):
        not_reserved = list(filter(lambda word: word not in self.reserved_words, self.word_to_index.keys()))
        words_to_keep = list(filter(lambda word: self.word_to_frequency[word] >= threshold, not_reserved))

        self.index_to_word.clear()
        self.word_to_index.clear()

        for item in self.reserved_words:
            self.add(item)
        for item in words_to_keep:
            self.add(item)

        self.word_to_frequency = {word: self.word_to_frequency[word] for word in self.word_to_index.keys()}

    def sort(self):
        not_reserved = list(filter(lambda key: key not in self.reserved_words, self.word_to_index.keys()))
        not_reserved.sort()

        self.index_to_word.clear()
        self.word_to_index.clear()

        for item in self.reserved_words:
            self.add(item)
        for item in not_reserved:
            self.add(item)
