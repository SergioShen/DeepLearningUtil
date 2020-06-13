#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 22:17 2018/2/2
# @Author: Shen Sijie
# @File: logger
# @Project: DeepLearningTemplates


import logging


def get_logger(log_path=None, mode='a'):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("[%(asctime)s] %(levelname)s: %(message)s")

    # File logger
    if log_path is not None:
        fh = logging.FileHandler(log_path, mode=mode)
        fh.setLevel(logging.INFO)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    # Console logger
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    return logger
