# -*- coding: utf-8 -*-

import numpy as np


class NNClassifier:

    def __init__(self):
        pass

    def classify(self, cache_file):
        x = []
        ceps = np.load(cache_file)
        num_ceps = len(ceps)
        x.append(np.mean(ceps[int(num_ceps / 10):int(num_ceps * 9 / 10)], axis=0))
        vx = np.array(x)
        print vx.shape
        # use Vx as input values vector for neural net, k-means, etc
