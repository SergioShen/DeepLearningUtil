#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 22:17 2018/2/2
# @Author: Shen Sijie
# @File: logger
# @Project: DeepLearningTemplates


import logging
import os


def get_logger(log_path=None, override=False):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("[%(asctime)s] %(levelname)s: %(message)s")

    # File logger
    if log_path is not None:
        if os.path.exists(log_path) and not override:
            raise FileExistsError

        fh = logging.FileHandler(log_path, mode='w')
        fh.setLevel(logging.INFO)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    # Console logger
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    return logger
