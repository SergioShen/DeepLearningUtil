#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 00:19 2020/9/29
# @Author: Sijie Shen
# @File: subtokenizer
# @Project: DeepLearningUtil

class Subtokenizer:
    UNDER_SCORE = 1
    NUM = 2
    UPPER = 3
    LOWER = 4

    def __init__(self, name, underscore_single=True):
        self.name = name
        self.underscore_single = underscore_single
        self.pos = 0

    def _check_stop(self):
        if self.pos == len(self.name):
            raise StopIteration

    @staticmethod
    def _get_char_type(char):
        if char == '_':
            return Subtokenizer.UNDER_SCORE
        elif char.isnumeric():
            return Subtokenizer.NUM
        elif char.islower():
            return Subtokenizer.LOWER
        elif char.isupper():
            return Subtokenizer.UPPER
        else:
            raise SyntaxError

    def __iter__(self):
        return self

    def __next__(self):
        self._check_stop()
        result = self.name[self.pos]  # The first letter
        self.pos += 1

        last_char_type = self._get_char_type(result)

        if last_char_type == Subtokenizer.UNDER_SCORE and self.underscore_single:
            return result

        while self.pos < len(self.name):
            current_char_type = self._get_char_type(self.name[self.pos])
            if current_char_type == Subtokenizer.UNDER_SCORE:
                return result
            elif current_char_type == Subtokenizer.NUM:
                if last_char_type == Subtokenizer.NUM:
                    result += self.name[self.pos]
                    self.pos += 1
                else:
                    return result
            elif current_char_type == Subtokenizer.LOWER:
                result += self.name[self.pos]
                self.pos += 1
            elif current_char_type == Subtokenizer.UPPER:
                if last_char_type == Subtokenizer.UPPER:
                    if self.pos + 1 < len(self.name) and self._get_char_type(
                            self.name[self.pos + 1]) != Subtokenizer.UPPER:
                        return result
                    else:
                        result += self.name[self.pos]
                        self.pos += 1
                else:
                    return result
            last_char_type = current_char_type

        return result


def subtokenize(name, underscore_single=True):
    subtokenizer = Subtokenizer(name, underscore_single)
    subtokens = list(subtokenizer)

    return subtokens


def subtokenize_tokens(tokens, lower=False, underscore_single=True, return_lengths=False):
    result = list()
    lengths = list()
    for token in tokens:
        if token[0] == '_' or token[0].isalpha():
            # This is an identifier, sub-tokenize it
            subtokens = subtokenize(token, underscore_single)
            for i in range(len(subtokens) - 1):
                if lower:
                    result.append((subtokens[i] + '@@').lower())
                else:
                    result.append(subtokens[i] + '@@')
            if lower:
                result.append(subtokens[-1].lower())
            else:
                result.append(subtokens[-1])
            lengths.append(len(subtokens))
        else:
            if lower:
                result.append(token.lower())
            else:
                result.append(token)
            lengths.append(1)

    if return_lengths:
        return result, lengths
    else:
        return result
