# -*- coding: utf-8 -*-

import numpy as np
from pybrain2.tools.customxml.networkreader import NetworkReader


class NNClassifier:

    def __init__(self, model):
        self.net = NetworkReader.readFrom(model)
        self.accents = [
            "CH",
            "EN",
            "IN",
            "IR",
            "IT",
            "JA",
            "KO",
        ]

    def classify(self, cache_file):
        x = []
        ceps = np.load(cache_file)
        num_ceps = len(ceps)
        x.append(np.mean(ceps[int(num_ceps / 10):int(num_ceps * 9 / 10)], axis=0))
        vx = np.array(x)

        result = self.net.activate(vx[0].tolist()).tolist()
        prob = max(result)
        accent = self.accents[result.index(prob)]

        print accent, prob
        return accent, prob
