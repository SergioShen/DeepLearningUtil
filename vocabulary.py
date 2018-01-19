#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 5:50 2018/1/19
# @Author: Shen Sijie
# @File: vocab
# @Project: DeepLearningTemplates


import copy
import os


class Vocabulary(object):
    """
    Implement of vocabulary
    """

    def __init__(self, reserved_words=None):
        """
        Create a vocabulary
        :param reserved_words: reserved words that won't change
        """
        self.index_to_word = {}
        self.word_to_index = {}
        self.reserved_words = []
        self.word_to_frequency = {}

        if reserved_words is not None:
            self.reserved_words = copy.deepcopy(reserved_words)
            for item in reserved_words:
                self.add(item)

    def size(self):
        """
        Get size of vocabulary
        :return: size of vocabulary
        """
        return len(self.index_to_word)

    def get_index(self, word, default=None):
        """
        Get index from word
        :param word: input word
        :param default: return value when *word* is not in vocabulary
        :return: index of *word*, or *default* if *word* is not in the vocabulary
        """
        try:
            return self.word_to_index[word]
        except KeyError:
            return default

    def get_word(self, index, default=None):
        """
        Get word from index
        :param index: input index
        :param default: return value when *index* is out of boundary
        :return: word linked to *index*, or *default* if *index* is out of boundary
        """
        try:
            return self.index_to_word[index]
        except KeyError:
            return default

    def add(self, word):
        """
        Add a word into vocabulary
        :param word: word to add
        :return: index of the just-added word
        """
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
        """
        Get all the words in the vocabulary
        :return: a list of all the words in the vocabulary
        """
        return self.word_to_index.keys()

    def delete_low_frequency_words(self, threshold):
        """
        Delete all the words with frequency lower than *threshold*
        :param threshold: threshold of word frequency
        :return: None
        """
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
        """
        Sort the vocabulary, with reserved words unchanged
        :return: None
        """
        not_reserved = list(filter(lambda key: key not in self.reserved_words, self.word_to_index.keys()))
        not_reserved.sort()

        self.index_to_word.clear()
        self.word_to_index.clear()

        for item in self.reserved_words:
            self.add(item)
        for item in not_reserved:
            self.add(item)

    def save(self, path, override=False):
        """
        Save vocabulary to a file
        :param path: save path
        :param override: override the file if *path* already exists
        :return: None
        """
        if not override and os.path.exists(path):
            raise FileExistsError

        file = open(path, 'w')
        for index in range(self.size()):
            file.write(self.index_to_word[index] + '\n')
        file.close()

    def load(self, path):
        """
        Load vocabulary from file
        :param path: vocabulary path
        :return: None
        """
        if not os.path.exists(path):
            raise FileNotFoundError

        file = open(path, 'r')
        for line in file:
            self.add(line.strip())
        file.close()
